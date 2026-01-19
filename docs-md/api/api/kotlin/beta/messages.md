# Messages

Copy page

Kotlin

# Messages

##### [Create a Message](api/beta/messages/create.md)

beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessage](api/beta.md)

post/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageTokensCount](api/beta.md)

post/v1/messages/count\_tokens

##### ModelsExpand Collapse

class BetaAllThinkingTurns:

type: JsonValue; "all"constant"all"constant

Accepts one of the following:

ALL("all")

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaBashCodeExecutionOutputBlock:

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

class BetaBashCodeExecutionOutputBlockParam:

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

class BetaBashCodeExecutionResultBlockParam:

content: List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlockParam:

content: List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaCacheControlEphemeral:

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCacheCreation:

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationConfig:

enabled: Boolean

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationsConfigParam:

enabled: Optional<Boolean>

class BetaCitationsDelta:

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaClearThinking20251015Edit:

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

keep: Optional<Keep>

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

type: JsonValue; "thinking\_turns"constant"thinking\_turns"constant

Accepts one of the following:

THINKING\_TURNS("thinking\_turns")

value: Long

class BetaAllThinkingTurns:

type: JsonValue; "all"constant"all"constant

Accepts one of the following:

ALL("all")

JsonValue;

Accepts one of the following:

ALL("all")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

class BetaClearToolUses20250919Edit:

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

clearAtLeast: Optional<[BetaInputTokensClearAtLeast](api/beta.md)>

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

clearToolInputs: Optional<ClearToolInputs>

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

List<String>

excludeTools: Optional<List<String>>

Tool names whose uses are preserved from clearing

keep: Optional<[BetaToolUsesKeep](api/beta.md)>

Number of tool uses to retain in the conversation

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

trigger: Optional<Trigger>

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

class BetaToolUsesTrigger:

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaCodeExecutionOutputBlock:

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

class BetaCodeExecutionOutputBlockParam:

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

class BetaCodeExecutionTool20250522:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250522"constant"code\_execution\_20250522"constant

Accepts one of the following:

CODE\_EXECUTION\_20250522("code\_execution\_20250522")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaCodeExecutionTool20250825:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

class BetaCodeExecutionToolResultBlockParam:

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

enum class BetaCodeExecutionToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaContainer:

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerParams:

Container parameters with skills to be loaded.

id: Optional<String>

Container id

skills: Optional<List<[BetaSkillParams](api/beta.md)>>

List of skills to load in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: Optional<String>

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaContentBlock: A class that can be one of several variants.union

Response model for a file uploaded to the container.

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

class BetaContentBlockParam: A class that can be one of several variants.union

Regular text content.

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlockParam:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaToolResultBlockParam:

toolUseId: String

type: JsonValue; "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

isError: Optional<Boolean>

class BetaServerToolUseBlockParam:

id: String

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaWebSearchToolResultBlockParam:

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaWebFetchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlockParam:

content: [BetaRequestDocumentBlock](api/beta.md)

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlockParam:

content: List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

errorMessage: Optional<String>

class BetaTextEditorCodeExecutionViewResultBlockParam:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

class BetaTextEditorCodeExecutionCreateResultBlockParam:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlockParam:

toolReferences: List<[BetaToolReferenceBlockParam](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaMcpToolUseBlockParam:

id: String

input: Input

name: String

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestMcpToolResultBlockParam:

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

isError: Optional<Boolean>

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaContentBlockSourceContent: A class that can be one of several variants.union

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaContextManagementConfig:

edits: Optional<List<Edit>>

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

clearAtLeast: Optional<[BetaInputTokensClearAtLeast](api/beta.md)>

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

clearToolInputs: Optional<ClearToolInputs>

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

List<String>

excludeTools: Optional<List<String>>

Tool names whose uses are preserved from clearing

keep: Optional<[BetaToolUsesKeep](api/beta.md)>

Number of tool uses to retain in the conversation

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

trigger: Optional<Trigger>

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

class BetaToolUsesTrigger:

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

class BetaClearThinking20251015Edit:

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

keep: Optional<Keep>

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

type: JsonValue; "thinking\_turns"constant"thinking\_turns"constant

Accepts one of the following:

THINKING\_TURNS("thinking\_turns")

value: Long

class BetaAllThinkingTurns:

type: JsonValue; "all"constant"all"constant

Accepts one of the following:

ALL("all")

JsonValue;

Accepts one of the following:

ALL("all")

class BetaContextManagementResponse:

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

class BetaCountTokensContextManagementResponse:

originalInputTokens: Long

The original token count before context management was applied

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaDocumentBlock:

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaInputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class BetaInputTokensClearAtLeast:

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

class BetaInputTokensTrigger:

type: JsonValue; "input\_tokens"constant"input\_tokens"constant

Accepts one of the following:

INPUT\_TOKENS("input\_tokens")

value: Long

class BetaJsonOutputFormat:

schema: Schema

The JSON schema of the format

type: JsonValue; "json\_schema"constant"json\_schema"constant

Accepts one of the following:

JSON\_SCHEMA("json\_schema")

class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolUseBlockParam:

id: String

input: Input

name: String

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcpServerName: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: JsonValue; "mcp\_toolset"constant"mcp\_toolset"constant

Accepts one of the following:

MCP\_TOOLSET("mcp\_toolset")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

configs: Optional<Configs>

Configuration overrides for specific tools, keyed by tool name

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

defaultConfig: Optional<[BetaMcpToolDefaultConfig](api/beta.md)>

Default configuration applied to all tools from this server

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

class BetaMemoryTool20250818:

name: JsonValue; "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

type: JsonValue; "memory\_20250818"constant"memory\_20250818"constant

Accepts one of the following:

MEMORY\_20250818("memory\_20250818")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaMemoryTool20250818Command: A class that can be one of several variants.union

class BetaMemoryTool20250818ViewCommand:

command: JsonValue; "view"constant"view"constant

Command type identifier

Accepts one of the following:

VIEW("view")

path: String

Path to directory or file to view

viewRange: Optional<List<Long>>

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand:

command: JsonValue; "create"constant"create"constant

Command type identifier

Accepts one of the following:

CREATE("create")

fileText: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand:

command: JsonValue; "str\_replace"constant"str\_replace"constant

Command type identifier

Accepts one of the following:

STR\_REPLACE("str\_replace")

newStr: String

Text to replace with

oldStr: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand:

command: JsonValue; "insert"constant"insert"constant

Command type identifier

Accepts one of the following:

INSERT("insert")

insertLine: Long

Line number where text should be inserted

minimum1

insertText: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand:

command: JsonValue; "delete"constant"delete"constant

Command type identifier

Accepts one of the following:

DELETE("delete")

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand:

command: JsonValue; "rename"constant"rename"constant

Command type identifier

Accepts one of the following:

RENAME("rename")

newPath: String

New path for the file or directory

oldPath: String

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand:

command: JsonValue; "create"constant"create"constant

Command type identifier

Accepts one of the following:

CREATE("create")

fileText: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand:

command: JsonValue; "delete"constant"delete"constant

Command type identifier

Accepts one of the following:

DELETE("delete")

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand:

command: JsonValue; "insert"constant"insert"constant

Command type identifier

Accepts one of the following:

INSERT("insert")

insertLine: Long

Line number where text should be inserted

minimum1

insertText: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand:

command: JsonValue; "rename"constant"rename"constant

Command type identifier

Accepts one of the following:

RENAME("rename")

newPath: String

New path for the file or directory

oldPath: String

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand:

command: JsonValue; "str\_replace"constant"str\_replace"constant

Command type identifier

Accepts one of the following:

STR\_REPLACE("str\_replace")

newStr: String

Text to replace with

oldStr: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand:

command: JsonValue; "view"constant"view"constant

Command type identifier

Accepts one of the following:

VIEW("view")

path: String

Path to directory or file to view

viewRange: Optional<List<Long>>

Optional line range for viewing specific lines

class BetaMessage:

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class BetaMessageDeltaUsage:

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

class BetaMessageParam:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockParam](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlockParam:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaToolResultBlockParam:

toolUseId: String

type: JsonValue; "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

isError: Optional<Boolean>

class BetaServerToolUseBlockParam:

id: String

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaWebSearchToolResultBlockParam:

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaWebFetchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlockParam:

content: [BetaRequestDocumentBlock](api/beta.md)

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlockParam:

content: List<[BetaCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlockParam:

content: List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

errorMessage: Optional<String>

class BetaTextEditorCodeExecutionViewResultBlockParam:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

class BetaTextEditorCodeExecutionCreateResultBlockParam:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlockParam:

toolReferences: List<[BetaToolReferenceBlockParam](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaMcpToolUseBlockParam:

id: String

input: Input

name: String

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestMcpToolResultBlockParam:

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

isError: Optional<Boolean>

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

role: Role

Accepts one of the following:

USER("user")

ASSISTANT("assistant")

class BetaMessageTokensCount:

contextManagement: Optional<[BetaCountTokensContextManagementResponse](api/beta.md)>

Information about context management applied to the message.

originalInputTokens: Long

The original token count before context management was applied

inputTokens: Long

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata:

userId: Optional<String>

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class BetaOutputConfig:

effort: Optional<Effort>

All possible effort levels.

Accepts one of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaRawContentBlockDelta: A class that can be one of several variants.union

class BetaTextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class BetaInputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class BetaCitationsDelta:

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class BetaThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class BetaSignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

class BetaRawContentBlockDeltaEvent:

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class BetaInputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class BetaCitationsDelta:

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class BetaThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class BetaSignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

index: Long

type: JsonValue; "content\_block\_delta"constant"content\_block\_delta"constant

Accepts one of the following:

CONTENT\_BLOCK\_DELTA("content\_block\_delta")

class BetaRawContentBlockStartEvent:

contentBlock: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

index: Long

type: JsonValue; "content\_block\_start"constant"content\_block\_start"constant

Accepts one of the following:

CONTENT\_BLOCK\_START("content\_block\_start")

class BetaRawContentBlockStopEvent:

index: Long

type: JsonValue; "content\_block\_stop"constant"content\_block\_stop"constant

Accepts one of the following:

CONTENT\_BLOCK\_STOP("content\_block\_stop")

class BetaRawMessageDeltaEvent:

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Information about context management strategies applied during the request

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

delta: Delta

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

stopReason: Optional<[BetaStopReason](api/beta.md)>

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

type: JsonValue; "message\_delta"constant"message\_delta"constant

Accepts one of the following:

MESSAGE\_DELTA("message\_delta")

usage: [BetaMessageDeltaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

class BetaRawMessageStartEvent:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "message\_start"constant"message\_start"constant

Accepts one of the following:

MESSAGE\_START("message\_start")

class BetaRawMessageStopEvent:

type: JsonValue; "message\_stop"constant"message\_stop"constant

Accepts one of the following:

MESSAGE\_STOP("message\_stop")

class BetaRawMessageStreamEvent: A class that can be one of several variants.union

class BetaRawMessageStartEvent:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "message\_start"constant"message\_start"constant

Accepts one of the following:

MESSAGE\_START("message\_start")

class BetaRawMessageDeltaEvent:

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Information about context management strategies applied during the request

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

delta: Delta

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

stopReason: Optional<[BetaStopReason](api/beta.md)>

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

type: JsonValue; "message\_delta"constant"message\_delta"constant

Accepts one of the following:

MESSAGE\_DELTA("message\_delta")

usage: [BetaMessageDeltaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreationInputTokens: Optional<Long>

The cumulative number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The cumulative number of input tokens read from the cache.

minimum0

inputTokens: Optional<Long>

The cumulative number of input tokens which were used.

minimum0

outputTokens: Long

The cumulative number of output tokens which were used.

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

class BetaRawMessageStopEvent:

type: JsonValue; "message\_stop"constant"message\_stop"constant

Accepts one of the following:

MESSAGE\_STOP("message\_stop")

class BetaRawContentBlockStartEvent:

contentBlock: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

index: Long

type: JsonValue; "content\_block\_start"constant"content\_block\_start"constant

Accepts one of the following:

CONTENT\_BLOCK\_START("content\_block\_start")

class BetaRawContentBlockDeltaEvent:

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class BetaInputJsonDelta:

partialJson: String

type: JsonValue; "input\_json\_delta"constant"input\_json\_delta"constant

Accepts one of the following:

INPUT\_JSON\_DELTA("input\_json\_delta")

class BetaCitationsDelta:

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

type: JsonValue; "citations\_delta"constant"citations\_delta"constant

Accepts one of the following:

CITATIONS\_DELTA("citations\_delta")

class BetaThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class BetaSignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

index: Long

type: JsonValue; "content\_block\_delta"constant"content\_block\_delta"constant

Accepts one of the following:

CONTENT\_BLOCK\_DELTA("content\_block\_delta")

class BetaRawContentBlockStopEvent:

index: Long

type: JsonValue; "content\_block\_stop"constant"content\_block\_stop"constant

Accepts one of the following:

CONTENT\_BLOCK\_STOP("content\_block\_stop")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaRedactedThinkingBlockParam:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaRequestMcpServerToolConfiguration:

allowedTools: Optional<List<String>>

enabled: Optional<Boolean>

class BetaRequestMcpServerUrlDefinition:

name: String

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

authorizationToken: Optional<String>

toolConfiguration: Optional<[BetaRequestMcpServerToolConfiguration](api/beta.md)>

allowedTools: Optional<List<String>>

enabled: Optional<Boolean>

class BetaRequestMcpToolResultBlockParam:

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

isError: Optional<Boolean>

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUsage:

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaServerToolUseBlockParam:

id: String

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaSignatureDelta:

signature: String

type: JsonValue; "signature\_delta"constant"signature\_delta"constant

Accepts one of the following:

SIGNATURE\_DELTA("signature\_delta")

class BetaSkill:

A skill that was loaded in a container (response model).

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: Optional<String>

Skill version or 'latest' for most recent version

maxLength64

minLength1

enum class BetaStopReason:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaTextCitation: A class that can be one of several variants.union

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaTextCitationParam: A class that can be one of several variants.union

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaTextDelta:

text: String

type: JsonValue; "text\_delta"constant"text\_delta"constant

Accepts one of the following:

TEXT\_DELTA("text\_delta")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionCreateResultBlockParam:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

errorMessage: Optional<String>

class BetaTextEditorCodeExecutionViewResultBlockParam:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

class BetaTextEditorCodeExecutionCreateResultBlockParam:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

errorMessage: Optional<String>

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionViewResultBlockParam:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaThinkingBlockParam:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaThinkingConfigDisabled:

type: JsonValue; "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class BetaThinkingConfigEnabled:

budgetTokens: Long

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: JsonValue; "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class BetaThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class BetaThinkingConfigEnabled:

budgetTokens: Long

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: JsonValue; "enabled"constant"enabled"constant

Accepts one of the following:

ENABLED("enabled")

class BetaThinkingConfigDisabled:

type: JsonValue; "disabled"constant"disabled"constant

Accepts one of the following:

DISABLED("disabled")

class BetaThinkingDelta:

thinking: String

type: JsonValue; "thinking\_delta"constant"thinking\_delta"constant

Accepts one of the following:

THINKING\_DELTA("thinking\_delta")

class BetaThinkingTurns:

type: JsonValue; "thinking\_turns"constant"thinking\_turns"constant

Accepts one of the following:

THINKING\_TURNS("thinking\_turns")

value: Long

class BetaTool:

inputSchema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: JsonValue; "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

properties: Optional<Properties>

required: Optional<List<String>>

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional<String>

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

type: Optional<Type>

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20241022"constant"bash\_20241022"constant

Accepts one of the following:

BASH\_20241022("bash\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolBash20250124:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20250124"constant"bash\_20250124"constant

Accepts one of the following:

BASH\_20250124("bash\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

type: JsonValue; "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

type: JsonValue; "any"constant"any"constant

Accepts one of the following:

ANY("any")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: JsonValue; "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

type: JsonValue; "none"constant"none"constant

Accepts one of the following:

NONE("none")

class BetaToolChoiceAny:

The model will use any available tools.

type: JsonValue; "any"constant"any"constant

Accepts one of the following:

ANY("any")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

type: JsonValue; "auto"constant"auto"constant

Accepts one of the following:

AUTO("auto")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

type: JsonValue; "none"constant"none"constant

Accepts one of the following:

NONE("none")

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: JsonValue; "tool"constant"tool"constant

Accepts one of the following:

TOOL("tool")

disableParallelToolUse: Optional<Boolean>

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20241022"constant"computer\_20241022"constant

Accepts one of the following:

COMPUTER\_20241022("computer\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20250124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20250124"constant"computer\_20250124"constant

Accepts one of the following:

COMPUTER\_20250124("computer\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20251124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20251124"constant"computer\_20251124"constant

Accepts one of the following:

COMPUTER\_20251124("computer\_20251124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

enableZoom: Optional<Boolean>

Whether to enable an action to take a zoomed-in screenshot of the screen.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolReferenceBlock:

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolResultBlockParam:

toolUseId: String

type: JsonValue; "tool\_result"constant"tool\_result"constant

Accepts one of the following:

TOOL\_RESULT("tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

content: Optional<Content>

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

content: List<[BetaTextBlockParam](api/beta.md)>

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

source: String

title: String

type: JsonValue; "search\_result"constant"search\_result"constant

Accepts one of the following:

SEARCH\_RESULT("search\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

class BetaRequestDocumentBlock:

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

isError: Optional<Boolean>

class BetaToolSearchToolBm25\_20251119:

name: JsonValue; "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolSearchToolRegex20251119:

name: JsonValue; "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaToolSearchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlockParam:

toolReferences: List<[BetaToolReferenceBlockParam](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolResultErrorParam:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

class BetaToolSearchToolSearchResultBlockParam:

toolReferences: List<[BetaToolReferenceBlockParam](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

class BetaToolTextEditor20241022:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20241022"constant"text\_editor\_20241022"constant

Accepts one of the following:

TEXT\_EDITOR\_20241022("text\_editor\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250124:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Accepts one of the following:

TEXT\_EDITOR\_20250124("text\_editor\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250429:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Accepts one of the following:

TEXT\_EDITOR\_20250429("text\_editor\_20250429")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250728:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Accepts one of the following:

TEXT\_EDITOR\_20250728("text\_editor\_20250728")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

maxCharacters: Optional<Long>

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional<Boolean>

class BetaToolUnion: A class that can be one of several variants.union

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

class BetaTool:

inputSchema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: JsonValue; "object"constant"object"constant

Accepts one of the following:

OBJECT("object")

properties: Optional<Properties>

required: Optional<List<String>>

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: Optional<String>

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

type: Optional<Type>

Accepts one of the following:

CUSTOM("custom")

class BetaToolBash20241022:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20241022"constant"bash\_20241022"constant

Accepts one of the following:

BASH\_20241022("bash\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolBash20250124:

name: JsonValue; "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

BASH("bash")

type: JsonValue; "bash\_20250124"constant"bash\_20250124"constant

Accepts one of the following:

BASH\_20250124("bash\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaCodeExecutionTool20250522:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250522"constant"code\_execution\_20250522"constant

Accepts one of the following:

CODE\_EXECUTION\_20250522("code\_execution\_20250522")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaCodeExecutionTool20250825:

name: JsonValue; "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

CODE\_EXECUTION("code\_execution")

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolComputerUse20241022:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20241022"constant"computer\_20241022"constant

Accepts one of the following:

COMPUTER\_20241022("computer\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaMemoryTool20250818:

name: JsonValue; "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

MEMORY("memory")

type: JsonValue; "memory\_20250818"constant"memory\_20250818"constant

Accepts one of the following:

MEMORY\_20250818("memory\_20250818")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20250124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20250124"constant"computer\_20250124"constant

Accepts one of the following:

COMPUTER\_20250124("computer\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20241022:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20241022"constant"text\_editor\_20241022"constant

Accepts one of the following:

TEXT\_EDITOR\_20241022("text\_editor\_20241022")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolComputerUse20251124:

displayHeightPx: Long

The height of the display in pixels.

minimum1

displayWidthPx: Long

The width of the display in pixels.

minimum1

name: JsonValue; "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

COMPUTER("computer")

type: JsonValue; "computer\_20251124"constant"computer\_20251124"constant

Accepts one of the following:

COMPUTER\_20251124("computer\_20251124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

displayNumber: Optional<Long>

The X11 display number (e.g. 0, 1) for the display.

minimum0

enableZoom: Optional<Boolean>

Whether to enable an action to take a zoomed-in screenshot of the screen.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250124:

name: JsonValue; "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_EDITOR("str\_replace\_editor")

type: JsonValue; "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Accepts one of the following:

TEXT\_EDITOR\_20250124("text\_editor\_20250124")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250429:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Accepts one of the following:

TEXT\_EDITOR\_20250429("text\_editor\_20250429")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

strict: Optional<Boolean>

class BetaToolTextEditor20250728:

name: JsonValue; "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

STR\_REPLACE\_BASED\_EDIT\_TOOL("str\_replace\_based\_edit\_tool")

type: JsonValue; "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Accepts one of the following:

TEXT\_EDITOR\_20250728("text\_editor\_20250728")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

inputExamples: Optional<List<InputExample>>

maxCharacters: Optional<Long>

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional<Boolean>

class BetaWebSearchTool20250305:

name: JsonValue; "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "web\_search\_20250305"constant"web\_search\_20250305"constant

Accepts one of the following:

WEB\_SEARCH\_20250305("web\_search\_20250305")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blockedDomains: Optional<List<String>>

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

userLocation: Optional<UserLocation>

Parameters for the user's location. Used to provide more relevant search results.

type: JsonValue; "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

city: Optional<String>

The city of the user.

maxLength255

minLength1

country: Optional<String>

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional<String>

The region of the user.

maxLength255

minLength1

timezone: Optional<String>

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebFetchTool20250910:

name: JsonValue; "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_FETCH("web\_fetch")

type: JsonValue; "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant

Accepts one of the following:

WEB\_FETCH\_20250910("web\_fetch\_20250910")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

List of domains to allow fetching from

blockedDomains: Optional<List<String>>

List of domains to block fetching from

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional<Boolean>

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxContentTokens: Optional<Long>

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

class BetaToolSearchToolBm25\_20251119:

name: JsonValue; "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaToolSearchToolRegex20251119:

name: JsonValue; "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

type: Type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional<Boolean>

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcpServerName: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: JsonValue; "mcp\_toolset"constant"mcp\_toolset"constant

Accepts one of the following:

MCP\_TOOLSET("mcp\_toolset")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

configs: Optional<Configs>

Configuration overrides for specific tools, keyed by tool name

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

defaultConfig: Optional<[BetaMcpToolDefaultConfig](api/beta.md)>

Default configuration applied to all tools from this server

deferLoading: Optional<Boolean>

enabled: Optional<Boolean>

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaToolUseBlockParam:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaToolUsesKeep:

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

class BetaToolUsesTrigger:

type: JsonValue; "tool\_uses"constant"tool\_uses"constant

Accepts one of the following:

TOOL\_USES("tool\_uses")

value: Long

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaUsage:

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

class BetaWebFetchBlockParam:

content: [BetaRequestDocumentBlock](api/beta.md)

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910:

name: JsonValue; "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_FETCH("web\_fetch")

type: JsonValue; "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant

Accepts one of the following:

WEB\_FETCH\_20250910("web\_fetch\_20250910")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

List of domains to allow fetching from

blockedDomains: Optional<List<String>>

List of domains to block fetching from

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional<Boolean>

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxContentTokens: Optional<Long>

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaWebFetchToolResultBlockParam:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlockParam:

content: [BetaRequestDocumentBlock](api/beta.md)

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaContentBlockSource:

content: Content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<List<[BetaTextCitationParam](api/beta.md)>>

Accepts one of the following:

class BetaCitationCharLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocationParam:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationWebSearchResultLocationParam:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocationParam:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

class BetaImageBlockParam:

source: Source

Accepts one of the following:

class BetaBase64ImageSource:

data: String

mediaType: MediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaUrlImageSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileImageSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "image"constant"image"constant

Accepts one of the following:

IMAGE("image")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

type: JsonValue; "content"constant"content"constant

Accepts one of the following:

CONTENT("content")

class BetaUrlPdfSource:

type: JsonValue; "url"constant"url"constant

Accepts one of the following:

URL("url")

url: String

class BetaFileDocumentSource:

fileId: String

type: JsonValue; "file"constant"file"constant

Accepts one of the following:

FILE("file")

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

citations: Optional<[BetaCitationsConfigParam](api/beta.md)>

enabled: Optional<Boolean>

context: Optional<String>

title: Optional<String>

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchToolResultErrorBlockParam:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

enum class BetaWebFetchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

class BetaWebSearchResultBlock:

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

class BetaWebSearchResultBlockParam:

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchTool20250305:

name: JsonValue; "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

WEB\_SEARCH("web\_search")

type: JsonValue; "web\_search\_20250305"constant"web\_search\_20250305"constant

Accepts one of the following:

WEB\_SEARCH\_20250305("web\_search\_20250305")

allowedCallers: Optional<List<AllowedCaller>>

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

allowedDomains: Optional<List<String>>

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blockedDomains: Optional<List<String>>

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

deferLoading: Optional<Boolean>

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

maxUses: Optional<Long>

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional<Boolean>

userLocation: Optional<UserLocation>

Parameters for the user's location. Used to provide more relevant search results.

type: JsonValue; "approximate"constant"approximate"constant

Accepts one of the following:

APPROXIMATE("approximate")

city: Optional<String>

The city of the user.

maxLength255

minLength1

country: Optional<String>

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional<String>

The region of the user.

maxLength255

minLength1

timezone: Optional<String>

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

class BetaWebSearchToolResultBlockParam:

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

cacheControl: Optional<[BetaCacheControlEphemeral](api/beta.md)>

Create a cache control breakpoint at this content block.

type: JsonValue; "ephemeral"constant"ephemeral"constant

Accepts one of the following:

EPHEMERAL("ephemeral")

ttl: Optional<Ttl>

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union

List<[BetaWebSearchResultBlockParam](api/beta.md)>

encryptedContent: String

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

pageAge: Optional<String>

class BetaWebSearchToolRequestError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

enum class BetaWebSearchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

#### MessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

post/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : BatchListPage

get/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatch](api/beta.md)

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaDeletedMessageBatch](api/beta.md)

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [BetaMessageBatchIndividualResponse](api/beta.md)

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch:

id: String

ID of the Message Batch.

type: JsonValue; "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

MESSAGE\_BATCH\_DELETED("message\_batch\_deleted")

class BetaMessageBatch:

id: String

Unique object identifier.

The format and length of IDs may change over time.

archivedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancelInitiatedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

endedAt: Optional<LocalDateTime>

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expiresAt: LocalDateTime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processingStatus: ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

requestCounts: [BetaMessageBatchRequestCounts](api/beta.md)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

resultsUrl: Optional<String>

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: JsonValue; "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

MESSAGE\_BATCH("message\_batch")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

customId: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchRequestCounts:

canceled: Long

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Long

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Long

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Long

Number of requests in the Message Batch that are processing.

succeeded: Long

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

class BetaMessageBatchErroredResult:

error: [BetaErrorResponse](api/beta.md)

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError:

message: String

type: JsonValue; "invalid\_request\_error"constant"invalid\_request\_error"constant

Accepts one of the following:

INVALID\_REQUEST\_ERROR("invalid\_request\_error")

class BetaAuthenticationError:

message: String

type: JsonValue; "authentication\_error"constant"authentication\_error"constant

Accepts one of the following:

AUTHENTICATION\_ERROR("authentication\_error")

class BetaBillingError:

message: String

type: JsonValue; "billing\_error"constant"billing\_error"constant

Accepts one of the following:

BILLING\_ERROR("billing\_error")

class BetaPermissionError:

message: String

type: JsonValue; "permission\_error"constant"permission\_error"constant

Accepts one of the following:

PERMISSION\_ERROR("permission\_error")

class BetaNotFoundError:

message: String

type: JsonValue; "not\_found\_error"constant"not\_found\_error"constant

Accepts one of the following:

NOT\_FOUND\_ERROR("not\_found\_error")

class BetaRateLimitError:

message: String

type: JsonValue; "rate\_limit\_error"constant"rate\_limit\_error"constant

Accepts one of the following:

RATE\_LIMIT\_ERROR("rate\_limit\_error")

class BetaGatewayTimeoutError:

message: String

type: JsonValue; "timeout\_error"constant"timeout\_error"constant

Accepts one of the following:

TIMEOUT\_ERROR("timeout\_error")

class BetaApiError:

message: String

type: JsonValue; "api\_error"constant"api\_error"constant

Accepts one of the following:

API\_ERROR("api\_error")

class BetaOverloadedError:

message: String

type: JsonValue; "overloaded\_error"constant"overloaded\_error"constant

Accepts one of the following:

OVERLOADED\_ERROR("overloaded\_error")

requestId: Optional<String>

type: JsonValue; "error"constant"error"constant

Accepts one of the following:

ERROR("error")

type: JsonValue; "errored"constant"errored"constant

Accepts one of the following:

ERRORED("errored")

class BetaMessageBatchCanceledResult:

type: JsonValue; "canceled"constant"canceled"constant

Accepts one of the following:

CANCELED("canceled")

class BetaMessageBatchExpiredResult:

type: JsonValue; "expired"constant"expired"constant

Accepts one of the following:

EXPIRED("expired")

class BetaMessageBatchSucceededResult:

message: [BetaMessage](api/beta.md)

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: Optional<[BetaContainer](api/beta.md)>

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expiresAt: LocalDateTime

The time at which the container will expire.

formatdate-time

skills: Optional<List<[BetaSkill](api/beta.md)>>

Skills loaded in the container

skillId: String

Skill ID

maxLength64

minLength1

type: Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List<[BetaContentBlock](api/beta.md)>

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

class BetaTextBlock:

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

class BetaThinkingBlock:

signature: String

thinking: String

type: JsonValue; "thinking"constant"thinking"constant

Accepts one of the following:

THINKING("thinking")

class BetaRedactedThinkingBlock:

data: String

type: JsonValue; "redacted\_thinking"constant"redacted\_thinking"constant

Accepts one of the following:

REDACTED\_THINKING("redacted\_thinking")

class BetaToolUseBlock:

id: String

input: Input

name: String

type: JsonValue; "tool\_use"constant"tool\_use"constant

Accepts one of the following:

TOOL\_USE("tool\_use")

caller: Optional<Caller>

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

class BetaServerToolUseBlock:

id: String

caller: Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

type: JsonValue; "direct"constant"direct"constant

Accepts one of the following:

DIRECT("direct")

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

toolId: String

type: JsonValue; "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Accepts one of the following:

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

input: Input

name: Name

Accepts one of the following:

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

type: JsonValue; "server\_tool\_use"constant"server\_tool\_use"constant

Accepts one of the following:

SERVER\_TOOL\_USE("server\_tool\_use")

class BetaWebSearchToolResultBlock:

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError:

errorCode: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

type: JsonValue; "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT\_ERROR("web\_search\_tool\_result\_error")

List<[BetaWebSearchResultBlock](api/beta.md)>

encryptedContent: String

pageAge: Optional<String>

title: String

type: JsonValue; "web\_search\_result"constant"web\_search\_result"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT("web\_search\_result")

url: String

toolUseId: String

type: JsonValue; "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Accepts one of the following:

WEB\_SEARCH\_TOOL\_RESULT("web\_search\_tool\_result")

class BetaWebFetchToolResultBlock:

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

errorCode: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

type: JsonValue; "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT\_ERROR("web\_fetch\_tool\_result\_error")

class BetaWebFetchBlock:

content: [BetaDocumentBlock](api/beta.md)

citations: Optional<[BetaCitationConfig](api/beta.md)>

Citation configuration for the document

enabled: Boolean

source: Source

Accepts one of the following:

class BetaBase64PdfSource:

data: String

mediaType: JsonValue; "application/pdf"constant"application/pdf"constant

Accepts one of the following:

APPLICATION\_PDF("application/pdf")

type: JsonValue; "base64"constant"base64"constant

Accepts one of the following:

BASE64("base64")

class BetaPlainTextSource:

data: String

mediaType: JsonValue; "text/plain"constant"text/plain"constant

Accepts one of the following:

TEXT\_PLAIN("text/plain")

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

title: Optional<String>

The title of the document

type: JsonValue; "document"constant"document"constant

Accepts one of the following:

DOCUMENT("document")

retrievedAt: Optional<String>

ISO 8601 timestamp when the content was retrieved

type: JsonValue; "web\_fetch\_result"constant"web\_fetch\_result"constant

Accepts one of the following:

WEB\_FETCH\_RESULT("web\_fetch\_result")

url: String

Fetched content URL

toolUseId: String

type: JsonValue; "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Accepts one of the following:

WEB\_FETCH\_TOOL\_RESULT("web\_fetch\_tool\_result")

class BetaCodeExecutionToolResultBlock:

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError:

errorCode: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

type: JsonValue; "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("code\_execution\_tool\_result\_error")

class BetaCodeExecutionResultBlock:

content: List<[BetaCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "code\_execution\_output"constant"code\_execution\_output"constant

Accepts one of the following:

CODE\_EXECUTION\_OUTPUT("code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "code\_execution\_result"constant"code\_execution\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_RESULT("code\_execution\_result")

toolUseId: String

type: JsonValue; "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Accepts one of the following:

CODE\_EXECUTION\_TOOL\_RESULT("code\_execution\_tool\_result")

class BetaBashCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

type: JsonValue; "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("bash\_code\_execution\_tool\_result\_error")

class BetaBashCodeExecutionResultBlock:

content: List<[BetaBashCodeExecutionOutputBlock](api/beta.md)>

fileId: String

type: JsonValue; "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_OUTPUT("bash\_code\_execution\_output")

returnCode: Long

stderr: String

stdout: String

type: JsonValue; "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_RESULT("bash\_code\_execution\_result")

toolUseId: String

type: JsonValue; "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Accepts one of the following:

BASH\_CODE\_EXECUTION\_TOOL\_RESULT("bash\_code\_execution\_tool\_result")

class BetaTextEditorCodeExecutionToolResultBlock:

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

errorMessage: Optional<String>

type: JsonValue; "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT\_ERROR("text\_editor\_code\_execution\_tool\_result\_error")

class BetaTextEditorCodeExecutionViewResultBlock:

content: String

fileType: FileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

numLines: Optional<Long>

startLine: Optional<Long>

totalLines: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_VIEW\_RESULT("text\_editor\_code\_execution\_view\_result")

class BetaTextEditorCodeExecutionCreateResultBlock:

isFileUpdate: Boolean

type: JsonValue; "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_CREATE\_RESULT("text\_editor\_code\_execution\_create\_result")

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

lines: Optional<List<String>>

newLines: Optional<Long>

newStart: Optional<Long>

oldLines: Optional<Long>

oldStart: Optional<Long>

type: JsonValue; "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_STR\_REPLACE\_RESULT("text\_editor\_code\_execution\_str\_replace\_result")

toolUseId: String

type: JsonValue; "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Accepts one of the following:

TEXT\_EDITOR\_CODE\_EXECUTION\_TOOL\_RESULT("text\_editor\_code\_execution\_tool\_result")

class BetaToolSearchToolResultBlock:

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError:

errorCode: ErrorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

errorMessage: Optional<String>

type: JsonValue; "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT\_ERROR("tool\_search\_tool\_result\_error")

class BetaToolSearchToolSearchResultBlock:

toolReferences: List<[BetaToolReferenceBlock](api/beta.md)>

toolName: String

type: JsonValue; "tool\_reference"constant"tool\_reference"constant

Accepts one of the following:

TOOL\_REFERENCE("tool\_reference")

type: JsonValue; "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_SEARCH\_RESULT("tool\_search\_tool\_search\_result")

toolUseId: String

type: JsonValue; "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_RESULT("tool\_search\_tool\_result")

class BetaMcpToolUseBlock:

id: String

input: Input

name: String

The name of the MCP tool

serverName: String

The name of the MCP server

type: JsonValue; "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Accepts one of the following:

MCP\_TOOL\_USE("mcp\_tool\_use")

class BetaMcpToolResultBlock:

content: Content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

citations: Optional<List<[BetaTextCitation](api/beta.md)>>

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endCharIndex: Long

fileId: Optional<String>

startCharIndex: Long

type: JsonValue; "char\_location"constant"char\_location"constant

Accepts one of the following:

CHAR\_LOCATION("char\_location")

class BetaCitationPageLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endPageNumber: Long

fileId: Optional<String>

startPageNumber: Long

type: JsonValue; "page\_location"constant"page\_location"constant

Accepts one of the following:

PAGE\_LOCATION("page\_location")

class BetaCitationContentBlockLocation:

citedText: String

documentIndex: Long

documentTitle: Optional<String>

endBlockIndex: Long

fileId: Optional<String>

startBlockIndex: Long

type: JsonValue; "content\_block\_location"constant"content\_block\_location"constant

Accepts one of the following:

CONTENT\_BLOCK\_LOCATION("content\_block\_location")

class BetaCitationsWebSearchResultLocation:

citedText: String

encryptedIndex: String

title: Optional<String>

type: JsonValue; "web\_search\_result\_location"constant"web\_search\_result\_location"constant

Accepts one of the following:

WEB\_SEARCH\_RESULT\_LOCATION("web\_search\_result\_location")

url: String

class BetaCitationSearchResultLocation:

citedText: String

endBlockIndex: Long

searchResultIndex: Long

source: String

startBlockIndex: Long

title: Optional<String>

type: JsonValue; "search\_result\_location"constant"search\_result\_location"constant

Accepts one of the following:

SEARCH\_RESULT\_LOCATION("search\_result\_location")

text: String

type: JsonValue; "text"constant"text"constant

Accepts one of the following:

TEXT("text")

isError: Boolean

toolUseId: String

type: JsonValue; "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Accepts one of the following:

MCP\_TOOL\_RESULT("mcp\_tool\_result")

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

fileId: String

type: JsonValue; "container\_upload"constant"container\_upload"constant

Accepts one of the following:

CONTAINER\_UPLOAD("container\_upload")

contextManagement: Optional<[BetaContextManagementResponse](api/beta.md)>

Context management response.

Information about context management strategies applied during the request.

appliedEdits: List<AppliedEdit>

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedToolUses: Long

Number of tool uses that were cleared.

minimum0

type: JsonValue; "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_TOOL\_USES\_20250919("clear\_tool\_uses\_20250919")

class BetaClearThinking20251015EditResponse:

clearedInputTokens: Long

Number of input tokens cleared by this edit.

minimum0

clearedThinkingTurns: Long

Number of thinking turns that were cleared.

minimum0

type: JsonValue; "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Accepts one of the following:

CLEAR\_THINKING\_20251015("clear\_thinking\_20251015")

model: Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_3\_7\_SONNET\_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE\_3\_7\_SONNET\_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE\_3\_5\_HAIKU\_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE\_3\_5\_HAIKU\_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_4\_SONNET\_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Our most capable model

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE\_4\_OPUS\_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE\_3\_OPUS\_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE\_3\_OPUS\_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

role: JsonValue; "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

ASSISTANT("assistant")

stopReason: Optional<[BetaStopReason](api/beta.md)>

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

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

stopSequence: Optional<String>

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: JsonValue; "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

MESSAGE("message")

usage: [BetaUsage](api/beta.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cacheCreation: Optional<[BetaCacheCreation](api/beta.md)>

Breakdown of cached tokens by TTL

ephemeral1hInputTokens: Long

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral5mInputTokens: Long

The number of input tokens used to create the 5 minute cache entry.

minimum0

cacheCreationInputTokens: Optional<Long>

The number of input tokens used to create the cache entry.

minimum0

cacheReadInputTokens: Optional<Long>

The number of input tokens read from the cache.

minimum0

inputTokens: Long

The number of input tokens which were used.

minimum0

outputTokens: Long

The number of output tokens which were used.

minimum0

serverToolUse: Optional<[BetaServerToolUsage](api/beta.md)>

The number of server tool requests.

webFetchRequests: Long

The number of web fetch tool requests.

minimum0

webSearchRequests: Long

The number of web search tool requests.

minimum0

serviceTier: Optional<ServiceTier>

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

type: JsonValue; "succeeded"constant"succeeded"constant

Accepts one of the following:

SUCCEEDED("succeeded")

---

*Copyright © Anthropic. All rights reserved.*
