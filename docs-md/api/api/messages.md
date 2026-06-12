# Messages

Copy page

SDK language

cURL

# Messages

##### [Create a Message](api/messages/create.md)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



BashCodeExecutionOutputBlock object { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"



BashCodeExecutionOutputBlockParam object { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"



BashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



BashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"



BashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



CacheControlEphemeral object { type, ttl } 

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



CacheCreation object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsConfig object { enabled } 

enabled: boolean



CitationsConfigParam object { enabled } 

enabled: optional boolean



CitationsDelta object { citation, type } 



citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CodeExecutionOutputBlock object { file\_id, type } 

file\_id: string

type: "code\_execution\_output"



CodeExecutionOutputBlockParam object { file\_id, type } 

file\_id: string

type: "code\_execution\_output"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



CodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



CodeExecutionToolResultBlockContent = [CodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [CodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlock](api/messages.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



CodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



CodeExecutionToolResultBlockParamContent = [CodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  or [CodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more }  or [EncryptedCodeExecutionResultBlockParam](api/messages.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



Container object { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



ContainerUploadBlockParam object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ContentBlock = [TextBlock](api/messages.md) { citations, text, type }  or [ThinkingBlock](api/messages.md) { signature, thinking, type }  or [RedactedThinkingBlock](api/messages.md) { data, type }  or 9 more

Response model for a file uploaded to the container.

One of the following:



TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



ContentBlockParam = [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more }  or 14 more

Regular text content.

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



ThinkingBlockParam object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlockParam object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



ToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



content: optional string or array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:

string



array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



ToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

is\_error: optional boolean



ServerToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  or [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at } 

One of the following:



WebFetchToolResultErrorBlockParam object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



CodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



BashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



TextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



TextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



TextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



ToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ContainerUploadBlockParam object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



MidConversationSystemBlockParam object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



ContentBlockSourceContent = [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control } 

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



DocumentBlock object { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



InputJSONDelta object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



JSONOutputFormat object { schema, type } 

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



MemoryTool20250818 object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



Message object { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



MessageCountTokensTool = [Tool](api/messages.md) { input\_schema, name, allowed\_callers, 7 more }  or [ToolBash20250124](api/messages.md) { name, type, allowed\_callers, 4 more }  or [CodeExecutionTool20250522](api/messages.md) { name, type, allowed\_callers, 3 more }  or 13 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



Tool object { input\_schema, name, allowed\_callers, 7 more } 

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

maxLength128

minLength1



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

type: optional "custom"



ToolBash20250124 object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



MemoryTool20250818 object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250124 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250429 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250728 object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

WebSearchTool20250305 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebFetchTool20250910 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebSearchTool20260209 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebFetchTool20260209 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebFetchTool20260309 object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

ToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



MessageDeltaUsage object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more } 

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



MessageParam object { content, role } 



content: string or array of [ContentBlockParam](api/messages.md)

One of the following:

string



array of [ContentBlockParam](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



ThinkingBlockParam object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlockParam object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



ToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



content: optional string or array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:

string



array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



ToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

is\_error: optional boolean



ServerToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  or [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at } 

One of the following:



WebFetchToolResultErrorBlockParam object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



CodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlockParam object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



BashCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [BashCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlockParam](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultErrorParam object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlockParam object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlockParam](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



TextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



TextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



TextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



ToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ContainerUploadBlockParam object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



MidConversationSystemBlockParam object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



role: "user" or "assistant" or "system"

One of the following:

"user"

"assistant"

"system"



MessageTokensCount object { input\_tokens } 

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.



Metadata object { user\_id } 



user\_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



MidConversationSystemBlockParam object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



Model = "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



OutputConfig object { effort, format } 



effort: optional "low" or "medium" or "high" or 2 more

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format: optional [JSONOutputFormat](api/messages.md) { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



OutputTokensDetails object { thinking\_tokens } 



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



RawContentBlockDelta = [TextDelta](api/messages.md) { text, type }  or [InputJSONDelta](api/messages.md) { partial\_json, type }  or [CitationsDelta](api/messages.md) { citation, type }  or 2 more

One of the following:



TextDelta object { text, type } 

text: string

type: "text\_delta"



InputJSONDelta object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



CitationsDelta object { citation, type } 



citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



ThinkingDelta object { thinking, type } 

thinking: string

type: "thinking\_delta"



SignatureDelta object { signature, type } 

signature: string

type: "signature\_delta"



RawContentBlockDeltaEvent object { delta, index, type } 



delta: [RawContentBlockDelta](api/messages.md)

One of the following:



TextDelta object { text, type } 

text: string

type: "text\_delta"



InputJSONDelta object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



CitationsDelta object { citation, type } 



citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



ThinkingDelta object { thinking, type } 

thinking: string

type: "thinking\_delta"



SignatureDelta object { signature, type } 

signature: string

type: "signature\_delta"

index: number

type: "content\_block\_delta"



RawContentBlockStartEvent object { content\_block, index, type } 



content\_block: [TextBlock](api/messages.md) { citations, text, type }  or [ThinkingBlock](api/messages.md) { signature, thinking, type }  or [RedactedThinkingBlock](api/messages.md) { data, type }  or 9 more

Response model for a file uploaded to the container.

One of the following:



TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

index: number

type: "content\_block\_start"



RawContentBlockStopEvent object { index, type } 

index: number

type: "content\_block\_stop"



RawMessageDeltaEvent object { delta, type, usage } 



delta: object { container, stop\_details, stop\_reason, stop\_sequence } 



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: string

type: "message\_delta"



usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more } 

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

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



RawMessageStartEvent object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "message\_start"



RawMessageStopEvent object { type } 

type: "message\_stop"



RawMessageStreamEvent = [RawMessageStartEvent](api/messages.md) { message, type }  or [RawMessageDeltaEvent](api/messages.md) { delta, type, usage }  or [RawMessageStopEvent](api/messages.md) { type }  or 3 more

One of the following:



RawMessageStartEvent object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "message\_start"



RawMessageDeltaEvent object { delta, type, usage } 



delta: object { container, stop\_details, stop\_reason, stop\_sequence } 



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: string

type: "message\_delta"



usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more } 

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

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



RawMessageStopEvent object { type } 

type: "message\_stop"



RawContentBlockStartEvent object { content\_block, index, type } 



content\_block: [TextBlock](api/messages.md) { citations, text, type }  or [ThinkingBlock](api/messages.md) { signature, thinking, type }  or [RedactedThinkingBlock](api/messages.md) { data, type }  or 9 more

Response model for a file uploaded to the container.

One of the following:



TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

index: number

type: "content\_block\_start"



RawContentBlockDeltaEvent object { delta, index, type } 



delta: [RawContentBlockDelta](api/messages.md)

One of the following:



TextDelta object { text, type } 

text: string

type: "text\_delta"



InputJSONDelta object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



CitationsDelta object { citation, type } 



citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



ThinkingDelta object { thinking, type } 

thinking: string

type: "thinking\_delta"



SignatureDelta object { signature, type } 

signature: string

type: "signature\_delta"

index: number

type: "content\_block\_delta"



RawContentBlockStopEvent object { index, type } 

index: number

type: "content\_block\_stop"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



RedactedThinkingBlockParam object { data, type } 

data: string

type: "redacted\_thinking"



RefusalStopDetails object { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



ServerToolUsage object { web\_fetch\_requests, web\_search\_requests } 

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



ServerToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



SignatureDelta object { signature, type } 

signature: string

type: "signature\_delta"



StopReason = "end\_turn" or "max\_tokens" or "stop\_sequence" or 3 more

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"



TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



TextCitation = [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



TextCitationParam = [CitationCharLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  or [CitationPageLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  or [CitationContentBlockLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  or 2 more

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



TextDelta object { text, type } 

text: string

type: "text\_delta"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [TextEditorCodeExecutionToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [TextEditorCodeExecutionViewResultBlockParam](api/messages.md) { content, file\_type, type, 3 more }  or [TextEditorCodeExecutionCreateResultBlockParam](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md) { type, lines, new\_lines, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



TextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



TextEditorCodeExecutionCreateResultBlockParam object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"



TextEditorCodeExecutionToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionViewResultBlockParam object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



ThinkingBlockParam object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



ThinkingConfigAdaptive object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



ThinkingConfigDisabled object { type } 

type: "disabled"



ThinkingConfigEnabled object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



ThinkingConfigParam = [ThinkingConfigEnabled](api/messages.md) { budget\_tokens, type, display }  or [ThinkingConfigDisabled](api/messages.md) { type }  or [ThinkingConfigAdaptive](api/messages.md) { type, display } 

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:



ThinkingConfigEnabled object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: "enabled"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



ThinkingConfigDisabled object { type } 

type: "disabled"



ThinkingConfigAdaptive object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



ThinkingDelta object { thinking, type } 

thinking: string

type: "thinking\_delta"



Tool object { input\_schema, name, allowed\_callers, 7 more } 

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

maxLength128

minLength1



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

type: optional "custom"



ToolBash20250124 object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolChoice = [ToolChoiceAuto](api/messages.md) { type, disable\_parallel\_tool\_use }  or [ToolChoiceAny](api/messages.md) { type, disable\_parallel\_tool\_use }  or [ToolChoiceTool](api/messages.md) { name, type, disable\_parallel\_tool\_use }  or [ToolChoiceNone](api/messages.md) { type } 

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



ToolChoiceAuto object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



ToolChoiceAny object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceTool object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceNone object { type } 

The model will not be allowed to use tools.

type: "none"



ToolChoiceAny object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceAuto object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



ToolChoiceNone object { type } 

The model will not be allowed to use tools.

type: "none"



ToolChoiceTool object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolReferenceBlock object { tool\_name, type } 

tool\_name: string

type: "tool\_reference"



ToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ToolResultBlockParam object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



content: optional string or array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:

string



array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  or [ImageBlockParam](api/messages.md) { source, type, cache\_control }  or [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  or 2 more

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



SearchResultBlockParam object { content, source, title, 3 more } 



content: array of [TextBlockParam](api/messages.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean



DocumentBlockParam object { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string



ToolReferenceBlockParam object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

is\_error: optional boolean



ToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ToolSearchToolResultBlockParam object { content, tool\_use\_id, type, cache\_control } 



content: [ToolSearchToolResultErrorParam](api/messages.md) { error\_code, type, error\_message }  or [ToolSearchToolSearchResultBlockParam](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



ToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



ToolSearchToolResultErrorParam object { error\_code, type, error\_message } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"



ToolSearchToolSearchResultBlockParam object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlockParam](api/messages.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"



ToolTextEditor20250124 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250429 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250728 object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

ToolUnion = [Tool](api/messages.md) { input\_schema, name, allowed\_callers, 7 more }  or [ToolBash20250124](api/messages.md) { name, type, allowed\_callers, 4 more }  or [CodeExecutionTool20250522](api/messages.md) { name, type, allowed\_callers, 3 more }  or 13 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



Tool object { input\_schema, name, allowed\_callers, 7 more } 

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

maxLength128

minLength1



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

type: optional "custom"



ToolBash20250124 object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20250522 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20250825 object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



CodeExecutionTool20260120 object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



MemoryTool20250818 object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250124 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250429 object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolTextEditor20250728 object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

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

WebSearchTool20250305 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebFetchTool20250910 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebSearchTool20260209 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebFetchTool20260209 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebFetchTool20260309 object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

ToolSearchToolBm25\_20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolSearchToolRegex20251119 object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ToolUseBlockParam object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



URLImageSource object { type, url } 

type: "url"

url: string



URLPDFSource object { type, url } 

type: "url"

url: string



Usage object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



UserLocation object { type, city, country, 2 more } 

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

WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

WebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved



WebFetchTool20250910 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebFetchTool20260209 object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebFetchTool20260309 object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

WebFetchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebFetchToolResultErrorBlockParam](api/messages.md) { error\_code, type }  or [WebFetchBlockParam](api/messages.md) { content, type, url, retrieved\_at } 

One of the following:



WebFetchToolResultErrorBlockParam object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlockParam object { content, type, url, retrieved\_at } 



content: [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } 



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type }  or [ContentBlockSource](api/messages.md) { content, type }  or [URLPDFSource](api/messages.md) { type, url } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



ContentBlockSource object { content, type } 



content: string or array of [ContentBlockSourceContent](api/messages.md)

One of the following:

string



ContentBlockSourceContent = array of [ContentBlockSourceContent](api/messages.md)

One of the following:



TextBlockParam object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional array of [TextCitationParam](api/messages.md)

One of the following:



CitationCharLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



CitationPageLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocationParam object { cited\_text, document\_index, document\_title, 3 more } 

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

CitationWebSearchResultLocationParam object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationSearchResultLocationParam object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



ImageBlockParam object { source, type, cache\_control } 



source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  or [URLImageSource](api/messages.md) { type, url } 

One of the following:



Base64ImageSource object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



URLImageSource object { type, url } 

type: "url"

url: string

type: "image"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

type: "content"



URLPDFSource object { type, url } 

type: "url"

url: string

type: "document"



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



citations: optional [CitationsConfigParam](api/messages.md) { enabled } 

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchToolResultErrorBlockParam object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchToolResultErrorCode = "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

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

WebSearchResultBlock object { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string



WebSearchResultBlockParam object { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



WebSearchTool20250305 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebSearchTool20260209 object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional [UserLocation](api/messages.md) { type, city, country, 2 more } 

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

WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebSearchToolResultBlockContent = [WebSearchToolResultError](api/messages.md) { error\_code, type }  or array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string



WebSearchToolResultBlockParam object { content, tool\_use\_id, type, 2 more } 



content: [WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

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

cache\_control: optional [CacheControlEphemeral](api/messages.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"

"1h"



caller: optional [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



WebSearchToolResultBlockParamContent = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more }  or [WebSearchToolRequestError](api/messages.md) { error\_code, type } 

One of the following:



WebSearchToolResultBlockItem = array of [WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



WebSearchToolRequestError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



WebSearchToolResultErrorCode = "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse



DeletedMessageBatch object { id, type } 

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



MessageBatch object { id, archived\_at, cancel\_initiated\_at, 7 more } 

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

formatdate-time

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: "in\_progress" or "canceling" or "ended"

Processing status of the Message Batch.

One of the following:

"in\_progress"

"canceling"

"ended"



request\_counts: [MessageBatchRequestCounts](api/messages.md) { canceled, errored, expired, 2 more } 

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

MessageBatchCanceledResult object { type } 

type: "canceled"



MessageBatchErroredResult object { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BillingError object { message, type } 

message: string

type: "billing\_error"



PermissionError object { message, type } 

message: string

type: "permission\_error"



NotFoundError object { message, type } 

message: string

type: "not\_found\_error"



RateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



APIErrorObject object { message, type } 

message: string

type: "api\_error"



OverloadedError object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



MessageBatchExpiredResult object { type } 

type: "expired"



MessageBatchIndividualResponse object { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"



MessageBatchErroredResult object { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BillingError object { message, type } 

message: string

type: "billing\_error"



PermissionError object { message, type } 

message: string

type: "permission\_error"



NotFoundError object { message, type } 

message: string

type: "not\_found\_error"



RateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



APIErrorObject object { message, type } 

message: string

type: "api\_error"



OverloadedError object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



MessageBatchCanceledResult object { type } 

type: "canceled"



MessageBatchExpiredResult object { type } 

type: "expired"



MessageBatchRequestCounts object { canceled, errored, expired, 2 more } 

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

MessageBatchResult = [MessageBatchSucceededResult](api/messages.md) { message, type }  or [MessageBatchErroredResult](api/messages.md) { error, type }  or [MessageBatchCanceledResult](api/messages.md) { type }  or [MessageBatchExpiredResult](api/messages.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"



MessageBatchErroredResult object { error, type } 



error: [ErrorResponse](api/$shared.md) { error, request\_id, type } 



error: [ErrorObject](api/$shared.md)

One of the following:



InvalidRequestError object { message, type } 

message: string

type: "invalid\_request\_error"



AuthenticationError object { message, type } 

message: string

type: "authentication\_error"



BillingError object { message, type } 

message: string

type: "billing\_error"



PermissionError object { message, type } 

message: string

type: "permission\_error"



NotFoundError object { message, type } 

message: string

type: "not\_found\_error"



RateLimitError object { message, type } 

message: string

type: "rate\_limit\_error"



GatewayTimeoutError object { message, type } 

message: string

type: "timeout\_error"



APIErrorObject object { message, type } 

message: string

type: "api\_error"



OverloadedError object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



MessageBatchCanceledResult object { type } 

type: "canceled"



MessageBatchExpiredResult object { type } 

type: "expired"



MessageBatchSucceededResult object { message, type } 



message: [Message](api/messages.md) { id, container, content, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: [Container](api/messages.md) { id, expires\_at } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



content: array of [ContentBlock](api/messages.md)

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

TextBlock object { citations, text, type } 



citations: array of [TextCitation](api/messages.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



CitationCharLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



CitationPageLocation object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



CitationContentBlockLocation object { cited\_text, document\_index, document\_title, 4 more } 

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

CitationsWebSearchResultLocation object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



CitationsSearchResultLocation object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 

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

minimum0

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



ThinkingBlock object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



RedactedThinkingBlock object { data, type } 

data: string

type: "redacted\_thinking"



ToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]

name: string

type: "tool\_use"



ServerToolUseBlock object { id, caller, input, 2 more } 

id: string



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"

input: map[unknown]



name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

One of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



WebSearchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebSearchToolResultBlockContent](api/messages.md)

One of the following:



WebSearchToolResultError object { error\_code, type } 



error\_code: [WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



array of [WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



WebFetchToolResultBlock object { caller, content, tool\_use\_id, type } 



caller: [DirectCaller](api/messages.md) { type }  or [ServerToolCaller](api/messages.md) { tool\_id, type }  or [ServerToolCaller20260120](api/messages.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



DirectCaller object { type } 

Tool invocation directly from the model.

type: "direct"



ServerToolCaller object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



ServerToolCaller20260120 object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



content: [WebFetchToolResultErrorBlock](api/messages.md) { error\_code, type }  or [WebFetchBlock](api/messages.md) { content, retrieved\_at, type, url } 

One of the following:



WebFetchToolResultErrorBlock object { error\_code, type } 



error\_code: [WebFetchToolResultErrorCode](api/messages.md)

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

type: "web\_fetch\_tool\_result\_error"



WebFetchBlock object { content, retrieved\_at, type, url } 



content: [DocumentBlock](api/messages.md) { citations, source, title, type } 



citations: [CitationsConfig](api/messages.md) { enabled } 

Citation configuration for the document

enabled: boolean



source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  or [PlainTextSource](api/messages.md) { data, media\_type, type } 

One of the following:



Base64PDFSource object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



PlainTextSource object { data, media\_type, type } 

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

CodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



CodeExecutionToolResultError object { error\_code, type } 



error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



CodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



EncryptedCodeExecutionResultBlock object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [CodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



BashCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [BashCodeExecutionToolResultError](api/messages.md) { error\_code, type }  or [BashCodeExecutionResultBlock](api/messages.md) { content, return\_code, stderr, 2 more } 

One of the following:



BashCodeExecutionToolResultError object { error\_code, type } 



error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



BashCodeExecutionResultBlock object { content, return\_code, stderr, 2 more } 



content: array of [BashCodeExecutionOutputBlock](api/messages.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



TextEditorCodeExecutionToolResultBlock object { content, tool\_use\_id, type } 



content: [TextEditorCodeExecutionToolResultError](api/messages.md) { error\_code, error\_message, type }  or [TextEditorCodeExecutionViewResultBlock](api/messages.md) { content, file\_type, num\_lines, 3 more }  or [TextEditorCodeExecutionCreateResultBlock](api/messages.md) { is\_file\_update, type }  or [TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



TextEditorCodeExecutionToolResultError object { error\_code, error\_message, type } 



error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



TextEditorCodeExecutionViewResultBlock object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

One of the following:

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



TextEditorCodeExecutionCreateResultBlock object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



TextEditorCodeExecutionStrReplaceResultBlock object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



ToolSearchToolResultBlock object { content, tool\_use\_id, type } 



content: [ToolSearchToolResultError](api/messages.md) { error\_code, error\_message, type }  or [ToolSearchToolSearchResultBlock](api/messages.md) { tool\_references, type } 

One of the following:



ToolSearchToolResultError object { error\_code, error\_message, type } 



error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



ToolSearchToolSearchResultBlock object { tool\_references, type } 



tool\_references: array of [ToolReferenceBlock](api/messages.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



ContainerUploadBlock object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

string



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [RefusalStopDetails](api/messages.md) { category, explanation, type } 

Structured information about a refusal.



category: "cyber" or "bio" or "reasoning\_extraction"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"

"bio"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"



stop\_reason: [StopReason](api/messages.md)

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

"refusal"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 6 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

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

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: [OutputTokensDetails](api/messages.md) { thinking\_tokens } 

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

minimum0



server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"

type: "succeeded"

---

*Copyright © Anthropic. All rights reserved.*
