# Messages

Copy page

Python

# Messages

##### [Create a Message](api/messages/create.md)

messages.create(MessageCreateParams\*\*kwargs)  -> [Message](api/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

messages.count\_tokens(MessageCountTokensParams\*\*kwargs)  -> [MessageTokensCount](api/messages.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class BashCodeExecutionOutputBlock: …

file\_id: str

type: Literal["bash\_code\_execution\_output"]

class BashCodeExecutionOutputBlockParam: …

file\_id: str

type: Literal["bash\_code\_execution\_output"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

class BashCodeExecutionResultBlockParam: …

content: List[[BashCodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlockParam: …

content: List[[BashCodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

class BashCodeExecutionToolResultErrorParam: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class CacheControlEphemeral: …

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class CacheCreation: …

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsConfig: …

enabled: bool

class CitationsConfigParam: …

enabled: Optional[bool]

class CitationsDelta: …

citation: Citation

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CodeExecutionOutputBlock: …

file\_id: str

type: Literal["code\_execution\_output"]

class CodeExecutionOutputBlockParam: …

file\_id: str

type: Literal["code\_execution\_output"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class CodeExecutionResultBlockParam: …

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class CodeExecutionTool20250522: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250522"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250825"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260120"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

[CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

class CodeExecutionToolResultBlockParam: …

content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlockParam: …

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

[CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlockParam: …

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

class CodeExecutionToolResultErrorParam: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class Container: …

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

class ContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

[ContentBlock](api/messages.md)

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 13 more]

Regular text content.

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class ToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional[Union[str, List[Content], null]]

Accepts one of the following:

str

List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class ToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: Optional[bool]

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class WebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlockParam: …

content: [DocumentBlockParam](api/messages.md)

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class CodeExecutionToolResultBlockParam: …

content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlockParam: …

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlockParam: …

content: List[[BashCodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class TextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]

class TextEditorCodeExecutionViewResultBlockParam: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

class TextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class ToolSearchToolResultErrorParam: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlockParam: …

tool\_references: List[[ToolReferenceBlockParam](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

[ContentBlockSourceContent](api/messages.md)

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class DocumentBlock: …

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

class JSONOutputFormat: …

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]

class MemoryTool20250818: …

name: Literal["memory"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["memory\_20250818"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class Message: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

[MessageCountTokensTool](api/messages.md)

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250522: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250522"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250825"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260120"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class MemoryTool20250818: …

name: Literal["memory"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["memory\_20250818"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250429"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250728"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20250305"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20250910"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260309: …

Web fetch tool with use\_cache parameter for bypassing cached content.

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260309"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class ToolSearchToolBm25\_20251119: …

name: Literal["tool\_search\_tool\_bm25"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_bm25\_20251119", "tool\_search\_tool\_bm25"]

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119: …

name: Literal["tool\_search\_tool\_regex"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_regex\_20251119", "tool\_search\_tool\_regex"]

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class MessageDeltaUsage: …

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

class MessageParam: …

content: Union[str, List[Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 14 more]]]

Accepts one of the following:

str

List[Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 14 more]]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class ToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional[Union[str, List[Content], null]]

Accepts one of the following:

str

List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class ToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: Optional[bool]

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class WebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlockParam: …

content: [DocumentBlockParam](api/messages.md)

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class CodeExecutionToolResultBlockParam: …

content: [CodeExecutionToolResultBlockParamContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultErrorParam: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlockParam: …

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultErrorParam: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlockParam: …

content: List[[BashCodeExecutionOutputBlockParam](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class TextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]

class TextEditorCodeExecutionViewResultBlockParam: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

class TextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class ToolSearchToolResultErrorParam: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlockParam: …

tool\_references: List[[ToolReferenceBlockParam](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: Literal["user", "assistant"]

Accepts one of the following:

"user"

"assistant"

class MessageTokensCount: …

input\_tokens: int

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata: …

user\_id: Optional[str]

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

Union[Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more], str]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

class OutputConfig: …

effort: Optional[Literal["low", "medium", "high", "max"]]

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: Optional[JSONOutputFormat]

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

[RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

class CitationsDelta: …

citation: Citation

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

class CitationsDelta: …

citation: Citation

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

index: int

type: Literal["content\_block\_delta"]

class RawContentBlockStartEvent: …

content\_block: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

index: int

type: Literal["content\_block\_start"]

class RawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]

class RawMessageDeltaEvent: …

delta: Delta

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

type: Literal["message\_delta"]

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

class RawMessageStartEvent: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["message\_start"]

class RawMessageStopEvent: …

type: Literal["message\_stop"]

[RawMessageStreamEvent](api/messages.md)

Accepts one of the following:

class RawMessageStartEvent: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["message\_start"]

class RawMessageDeltaEvent: …

delta: Delta

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

type: Literal["message\_delta"]

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

class RawMessageStopEvent: …

type: Literal["message\_stop"]

class RawContentBlockStartEvent: …

content\_block: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

index: int

type: Literal["content\_block\_start"]

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

class CitationsDelta: …

citation: Citation

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

index: int

type: Literal["content\_block\_delta"]

class RawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

class RefusalStopDetails: …

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class ServerToolUsage: …

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

Literal["end\_turn", "max\_tokens", "stop\_sequence", 3 more]

Accepts one of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

[TextCitation](api/messages.md)

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

[TextCitationParam](api/messages.md)

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class TextDelta: …

text: str

type: Literal["text\_delta"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

class TextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultErrorParam: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]

class TextEditorCodeExecutionViewResultBlockParam: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

class TextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

class TextEditorCodeExecutionToolResultErrorParam: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionViewResultBlockParam: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]

class ThinkingConfigAdaptive: …

type: Literal["adaptive"]

display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"

"omitted"

class ThinkingConfigDisabled: …

type: Literal["disabled"]

class ThinkingConfigEnabled: …

budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal["enabled"]

display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"

"omitted"

[ThinkingConfigParam](api/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class ThinkingConfigEnabled: …

budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal["enabled"]

display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"

"omitted"

class ThinkingConfigDisabled: …

type: Literal["disabled"]

class ThinkingConfigAdaptive: …

type: Literal["adaptive"]

display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

"summarized"

"omitted"

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

[ToolChoice](api/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]

class ToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolReferenceBlock: …

tool\_name: str

type: Literal["tool\_reference"]

class ToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional[Union[str, List[Content], null]]

Accepts one of the following:

str

List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

class DocumentBlockParam: …

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

class ToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is\_error: Optional[bool]

class ToolSearchToolBm25\_20251119: …

name: Literal["tool\_search\_tool\_bm25"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_bm25\_20251119", "tool\_search\_tool\_bm25"]

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119: …

name: Literal["tool\_search\_tool\_regex"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_regex\_20251119", "tool\_search\_tool\_regex"]

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class ToolSearchToolResultErrorParam: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlockParam: …

tool\_references: List[[ToolReferenceBlockParam](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

class ToolSearchToolResultErrorParam: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

class ToolSearchToolSearchResultBlockParam: …

tool\_references: List[[ToolReferenceBlockParam](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250429"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250728"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

[ToolUnion](api/messages.md)

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250522: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250522"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20250825: …

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250825"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class CodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260120"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class MemoryTool20250818: …

name: Literal["memory"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["memory\_20250818"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250124"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250429"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250728"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20250305"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20250910: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20250910"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20260209: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchTool20260209: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260309: …

Web fetch tool with use\_cache parameter for bypassing cached content.

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260309"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class ToolSearchToolBm25\_20251119: …

name: Literal["tool\_search\_tool\_bm25"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_bm25\_20251119", "tool\_search\_tool\_bm25"]

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolSearchToolRegex20251119: …

name: Literal["tool\_search\_tool\_regex"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["tool\_search\_tool\_regex\_20251119", "tool\_search\_tool\_regex"]

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class URLImageSource: …

type: Literal["url"]

url: str

class URLPDFSource: …

type: Literal["url"]

url: str

class Usage: …

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

class UserLocation: …

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

class WebFetchBlockParam: …

content: [DocumentBlockParam](api/messages.md)

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

class WebFetchTool20250910: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20250910"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260209: …

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebFetchTool20260309: …

Web fetch tool with use\_cache parameter for bypassing cached content.

name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260309"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class WebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlockParam: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlockParam: …

content: [DocumentBlockParam](api/messages.md)

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

str

List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[List[[TextCitationParam](api/messages.md)]]

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

class ImageBlockParam: …

source: Source

Accepts one of the following:

class Base64ImageSource: …

data: str

media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]

class URLImageSource: …

type: Literal["url"]

url: str

type: Literal["image"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal["content"]

class URLPDFSource: …

type: Literal["url"]

url: str

type: Literal["document"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional[CitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchToolResultErrorBlockParam: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

Literal["invalid\_tool\_input", "url\_too\_long", "url\_not\_allowed", 5 more]

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

class WebSearchResultBlock: …

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

class WebSearchResultBlockParam: …

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20250305"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebSearchTool20260209: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260209"]

allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120"]]]

Accepts one of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class WebSearchToolRequestError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

[WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional[Caller]

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

[WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

messages.batches.create(BatchCreateParams\*\*kwargs)  -> [MessageBatch](api/messages.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages.batches.retrieve(strmessage\_batch\_id)  -> [MessageBatch](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages.batches.list(BatchListParams\*\*kwargs)  -> SyncPage[[MessageBatch](api/messages.md)]

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages.batches.cancel(strmessage\_batch\_id)  -> [MessageBatch](api/messages.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages.batches.delete(strmessage\_batch\_id)  -> [DeletedMessageBatch](api/messages.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages.batches.results(strmessage\_batch\_id)  -> [MessageBatchIndividualResponse](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class DeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal["message\_batch\_deleted"]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class MessageBatch: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing\_status: Literal["in\_progress", "canceling", "ended"]

Processing status of the Message Batch.

Accepts one of the following:

"in\_progress"

"canceling"

"ended"

request\_counts: [MessageBatchRequestCounts](api/messages.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: Optional[str]

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: Literal["message\_batch"]

Object type.

For Message Batches, this is always `"message_batch"`.

class MessageBatchCanceledResult: …

type: Literal["canceled"]

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

class BillingError: …

message: str

type: Literal["billing\_error"]

class PermissionError: …

message: str

type: Literal["permission\_error"]

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

class APIErrorObject: …

message: str

type: Literal["api\_error"]

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]

class MessageBatchExpiredResult: …

type: Literal["expired"]

class MessageBatchIndividualResponse: …

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: str

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

class BillingError: …

message: str

type: Literal["billing\_error"]

class PermissionError: …

message: str

type: Literal["permission\_error"]

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

class APIErrorObject: …

message: str

type: Literal["api\_error"]

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]

class MessageBatchCanceledResult: …

type: Literal["canceled"]

class MessageBatchExpiredResult: …

type: Literal["expired"]

class MessageBatchRequestCounts: …

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

class BillingError: …

message: str

type: Literal["billing\_error"]

class PermissionError: …

message: str

type: Literal["permission\_error"]

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

class APIErrorObject: …

message: str

type: Literal["api\_error"]

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

request\_id: Optional[str]

type: Literal["error"]

type: Literal["errored"]

class MessageBatchCanceledResult: …

type: Literal["canceled"]

class MessageBatchExpiredResult: …

type: Literal["expired"]

class MessageBatchSucceededResult: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional[Container]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.

content: List[[ContentBlock](api/messages.md)]

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

class TextBlock: …

citations: Optional[List[[TextCitation](api/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

class ToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

class ServerToolUseBlock: …

id: str

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

input: Dict[str, object]

name: Literal["web\_search", "web\_fetch", "code\_execution", 4 more]

Accepts one of the following:

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]

class WebSearchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: [WebSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

class WebFetchToolResultBlock: …

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class DirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]

class ServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]

class ServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]

content: Content

Accepts one of the following:

class WebFetchToolResultErrorBlock: …

error\_code: [WebFetchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]

class WebFetchBlock: …

content: [DocumentBlock](api/messages.md)

citations: Optional[CitationsConfig]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]

class CodeExecutionToolResultBlock: …

content: [CodeExecutionToolResultBlockContent](api/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class CodeExecutionToolResultError: …

error\_code: [CodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]

class CodeExecutionResultBlock: …

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]

class EncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.

content: List[[CodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]

class BashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BashCodeExecutionToolResultError: …

error\_code: [BashCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]

class BashCodeExecutionResultBlock: …

content: List[[BashCodeExecutionOutputBlock](api/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]

class TextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class TextEditorCodeExecutionToolResultError: …

error\_code: [TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

class TextEditorCodeExecutionViewResultBlock: …

content: str

file\_type: Literal["text", "image", "pdf"]

Accepts one of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]

class TextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]

class TextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]

class ToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class ToolSearchToolResultError: …

error\_code: [ToolSearchToolResultErrorCode](api/messages.md)

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]

class ToolSearchToolSearchResultBlock: …

tool\_references: List[[ToolReferenceBlock](api/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]

class ContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-mythos-preview", "claude-opus-4-6", 14 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - New class of intelligence, strongest in coding and cybersecurity
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Exceptional model for specialized complex tasks
- `claude-opus-4-1-20250805` - Exceptional model for specialized complex tasks
- `claude-opus-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-0` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-sonnet-4-20250514` - Deprecated: Will reach end-of-life on June 15th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Deprecated: Will reach end-of-life on April 20th, 2026. Please migrate to claude-haiku-4-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

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

str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: Optional[RefusalStopDetails]

Structured information about a refusal.

category: Optional[Literal["cyber", "bio"]]

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

"cyber"

"bio"

explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: Literal["refusal"]

stop\_reason: Optional[StopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal["message"]

Object type.

For Messages, this is always `"message"`.

usage: [Usage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

---

*Copyright © Anthropic. All rights reserved.*
