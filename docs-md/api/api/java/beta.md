# Beta

Copy page

Java

# Beta

##### ModelsExpand Collapse

enum AnthropicBeta:

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaError: A class that can be one of several variants.union

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

class BetaErrorResponse:

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

#### BetaModels

##### [List Models](api/beta/models/list.md)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta.md) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaCapabilitySupport:

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class BetaContextManagementCapability:

Context management capability details.

Optional<[BetaCapabilitySupport](api/beta.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class BetaEffortCapability:

Effort (reasoning\_effort) capability details.

[BetaCapabilitySupport](api/beta.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class BetaModelCapabilities:

Model capability information.

[BetaCapabilitySupport](api/beta.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](api/beta.md) contextManagement

Context management support and available strategies.

Optional<[BetaCapabilitySupport](api/beta.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaEffortCapability](api/beta.md) effort

Effort (reasoning\_effort) support and available levels.

[BetaCapabilitySupport](api/beta.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingCapability](api/beta.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta.md) types

Supported thinking type configurations.

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class BetaModelInfo:

String id

Unique model identifier.

Optional<[BetaModelCapabilities](api/beta.md)> capabilities

Model capability information.

[BetaCapabilitySupport](api/beta.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](api/beta.md) contextManagement

Context management support and available strategies.

Optional<[BetaCapabilitySupport](api/beta.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaEffortCapability](api/beta.md) effort

Effort (reasoning\_effort) support and available levels.

[BetaCapabilitySupport](api/beta.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingCapability](api/beta.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta.md) types

Supported thinking type configurations.

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

Optional<Long> maxInputTokens

Maximum input context window size in tokens for this model.

Optional<Long> maxTokens

Maximum value for the `max_tokens` parameter when using this model.

JsonValue; type "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

class BetaThinkingCapability:

Thinking capability details.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta.md) types

Supported thinking type configurations.

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class BetaThinkingTypes:

Supported thinking type configurations.

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

[BetaMessage](api/beta.md) beta().messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

[BetaMessageTokensCount](api/beta.md) beta().messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorTool20260301:

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; name "advisor"constant"advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "advisor\_20260301"constant"advisor\_20260301"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCacheControlEphemeral](api/beta.md)> caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaAdvisorToolResultBlockParam:

Content content

Accepts one of the following:

class BetaAdvisorToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaBashCodeExecutionOutputBlock:

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

class BetaBashCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

class BetaBashCodeExecutionResultBlockParam:

List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaCacheControlEphemeral:

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCacheCreation:

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationConfig:

boolean enabled

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationsConfigParam:

Optional<Boolean> enabled

class BetaCitationsDelta:

Citation citation

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaClearThinking20251015Edit:

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

Optional<Keep> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

JsonValue;

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

class BetaClearToolUses20250919Edit:

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

Optional<[BetaInputTokensClearAtLeast](api/beta.md)> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

Optional<ClearToolInputs> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

List<String>

Optional<List<String>> excludeTools

Tool names whose uses are preserved from clearing

Optional<[BetaToolUsesKeep](api/beta.md)> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

Optional<Trigger> trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaCodeExecutionOutputBlock:

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

class BetaCodeExecutionOutputBlockParam:

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaCodeExecutionResultBlockParam:

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaCodeExecutionTool20250522:

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250522"constant"code\_execution\_20250522"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaCodeExecutionToolResultBlockContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web\_search results.

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union

Code execution result with encrypted stdout for PFC + web\_search results.

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

enum BetaCodeExecutionToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact\_20260112"constant"compact\_20260112"constant

Optional<String> instructions

Additional instructions for summarization.

Optional<Boolean> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

Optional<[BetaInputTokensTrigger](api/beta.md)> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Optional<String> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaContainer:

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

class BetaContainerParams:

Container parameters with skills to be loaded.

Optional<String> id

Container id

Optional<List<[BetaSkillParams](api/beta.md)>> skills

List of skills to load in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional<String> version

Skill version or 'latest' for most recent version

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

class BetaContentBlockParam: A class that can be one of several variants.union

Regular text content.

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError

class BetaServerToolUseBlockParam:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge

class BetaWebSearchToolRequestError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](api/beta.md) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlockParam:

Content content

Accepts one of the following:

class BetaAdvisorToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

List<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Optional<String> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaContentBlockSourceContent: A class that can be one of several variants.union

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaContextManagementConfig:

Optional<List<Edit>> edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

Optional<[BetaInputTokensClearAtLeast](api/beta.md)> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

Optional<ClearToolInputs> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

boolean

List<String>

Optional<List<String>> excludeTools

Tool names whose uses are preserved from clearing

Optional<[BetaToolUsesKeep](api/beta.md)> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

Optional<Trigger> trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

class BetaClearThinking20251015Edit:

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

Optional<Keep> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value

class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

JsonValue;

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact\_20260112"constant"compact\_20260112"constant

Optional<String> instructions

Additional instructions for summarization.

Optional<Boolean> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

Optional<[BetaInputTokensTrigger](api/beta.md)> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaContextManagementResponse:

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

class BetaCountTokensContextManagementResponse:

long originalInputTokens

The original token count before context management was applied

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaDocumentBlock:

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant

class BetaInputTokensClearAtLeast:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value

class BetaJsonOutputFormat:

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant

class BetaMcpToolConfig:

Configuration for a specific tool in an MCP toolset.

Optional<Boolean> deferLoading

Optional<Boolean> enabled

class BetaMcpToolDefaultConfig:

Default configuration for tools in an MCP toolset.

Optional<Boolean> deferLoading

Optional<Boolean> enabled

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

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

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp\_toolset"constant"mcp\_toolset"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Configs> configs

Configuration overrides for specific tools, keyed by tool name

Optional<Boolean> deferLoading

Optional<Boolean> enabled

Optional<[BetaMcpToolDefaultConfig](api/beta.md)> defaultConfig

Default configuration applied to all tools from this server

Optional<Boolean> deferLoading

Optional<Boolean> enabled

class BetaMemoryTool20250818:

JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory\_20250818"constant"memory\_20250818"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818Command: A class that can be one of several variants.union

class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

String path

Path to directory or file to view

Optional<List<Long>> viewRange

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

String fileText

Content to write to the file

String path

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str\_replace"constant"str\_replace"constant

Command type identifier

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

long insertLine

Line number where text should be inserted

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

String path

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand:

JsonValue; command "create"constant"create"constant

Command type identifier

String fileText

Content to write to the file

String path

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand:

JsonValue; command "delete"constant"delete"constant

Command type identifier

String path

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand:

JsonValue; command "insert"constant"insert"constant

Command type identifier

long insertLine

Line number where text should be inserted

String insertText

Text to insert at the specified line

String path

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand:

JsonValue; command "rename"constant"rename"constant

Command type identifier

String newPath

New path for the file or directory

String oldPath

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand:

JsonValue; command "str\_replace"constant"str\_replace"constant

Command type identifier

String newStr

Text to replace with

String oldStr

Text to search for and replace

String path

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand:

JsonValue; command "view"constant"view"constant

Command type identifier

String path

Path to directory or file to view

Optional<List<Long>> viewRange

Optional line range for viewing specific lines

class BetaMessage:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaMessageDeltaUsage:

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The cumulative number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaMessageParam:

Content content

Accepts one of the following:

String

List<[BetaContentBlockParam](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError

class BetaServerToolUseBlockParam:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge

class BetaWebSearchToolRequestError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](api/beta.md) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlockParam:

Content content

Accepts one of the following:

class BetaAdvisorToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCodeExecutionToolResultBlockParam:

[BetaCodeExecutionToolResultBlockParamContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaBashCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

List<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

List<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

Optional<String> content

Summary of previously compacted content, or null if compaction failed

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

Role role

Accepts one of the following:

USER("user")

ASSISTANT("assistant")

class BetaMessageTokensCount:

Optional<[BetaCountTokensContextManagementResponse](api/beta.md)> contextManagement

Information about context management applied to the message.

long originalInputTokens

The original token count before context management was applied

long inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata:

Optional<String> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

class BetaOutputConfig:

Optional<Effort> effort

All possible effort levels.

Accepts one of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")

Optional<[BetaJsonOutputFormat](api/beta.md)> format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant

Optional<[BetaTokenTaskBudget](api/beta.md)> taskBudget

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaRawContentBlockDelta: A class that can be one of several variants.union

class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant

class BetaCitationsDelta:

Citation citation

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant

class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant

class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

class BetaRawContentBlockDeltaEvent:

[BetaRawContentBlockDelta](api/beta.md) delta

Accepts one of the following:

class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant

class BetaCitationsDelta:

Citation citation

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant

class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant

class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

long index

JsonValue; type "content\_block\_delta"constant"content\_block\_delta"constant

class BetaRawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

long index

JsonValue; type "content\_block\_start"constant"content\_block\_start"constant

class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content\_block\_stop"constant"content\_block\_stop"constant

class BetaRawMessageDeltaEvent:

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Information about context management strategies applied during the request

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Delta delta

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

JsonValue; type "message\_delta"constant"message\_delta"constant

[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The cumulative number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class BetaRawMessageStartEvent:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "message\_start"constant"message\_start"constant

class BetaRawMessageStopEvent:

JsonValue; type "message\_stop"constant"message\_stop"constant

class BetaRawMessageStreamEvent: A class that can be one of several variants.union

class BetaRawMessageStartEvent:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "message\_start"constant"message\_start"constant

class BetaRawMessageDeltaEvent:

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Information about context management strategies applied during the request

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Delta delta

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

Accepts one of the following:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

JsonValue; type "message\_delta"constant"message\_delta"constant

[BetaMessageDeltaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<Long> cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The cumulative number of input tokens read from the cache.

Optional<Long> inputTokens

The cumulative number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The cumulative number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class BetaRawMessageStopEvent:

JsonValue; type "message\_stop"constant"message\_stop"constant

class BetaRawContentBlockStartEvent:

ContentBlock contentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock:

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

long index

JsonValue; type "content\_block\_start"constant"content\_block\_start"constant

class BetaRawContentBlockDeltaEvent:

[BetaRawContentBlockDelta](api/beta.md) delta

Accepts one of the following:

class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant

class BetaInputJsonDelta:

String partialJson

JsonValue; type "input\_json\_delta"constant"input\_json\_delta"constant

class BetaCitationsDelta:

Citation citation

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "citations\_delta"constant"citations\_delta"constant

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant

class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant

class BetaCompactionContentBlockDelta:

Optional<String> content

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction\_delta"constant"compaction\_delta"constant

long index

JsonValue; type "content\_block\_delta"constant"content\_block\_delta"constant

class BetaRawContentBlockStopEvent:

long index

JsonValue; type "content\_block\_stop"constant"content\_block\_stop"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaRefusalStopDetails:

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaRequestMcpServerToolConfiguration:

Optional<List<String>> allowedTools

Optional<Boolean> enabled

class BetaRequestMcpServerUrlDefinition:

String name

JsonValue; type "url"constant"url"constant

String url

Optional<String> authorizationToken

Optional<[BetaRequestMcpServerToolConfiguration](api/beta.md)> toolConfiguration

Optional<List<String>> allowedTools

Optional<Boolean> enabled

class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<[BetaTextBlockParam](api/beta.md)>

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUsage:

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlockParam:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaSignatureDelta:

String signature

JsonValue; type "signature\_delta"constant"signature\_delta"constant

class BetaSkill:

A skill that was loaded in a container (response model).

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

class BetaSkillParams:

Specification for a skill to be loaded in a container (request model).

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional<String> version

Skill version or 'latest' for most recent version

enum BetaStopReason:

END\_TURN("end\_turn")

MAX\_TOKENS("max\_tokens")

STOP\_SEQUENCE("stop\_sequence")

TOOL\_USE("tool\_use")

PAUSE\_TURN("pause\_turn")

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

class BetaTextBlock:

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaTextCitation: A class that can be one of several variants.union

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaTextCitationParam: A class that can be one of several variants.union

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaTextDelta:

String text

JsonValue; type "text\_delta"constant"text\_delta"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlockParam:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionViewResultBlockParam:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

SUMMARIZED("summarized")

OMITTED("omitted")

class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

SUMMARIZED("summarized")

OMITTED("omitted")

class BetaThinkingConfigParam: A class that can be one of several variants.union

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

class BetaThinkingConfigEnabled:

long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant

Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

SUMMARIZED("summarized")

OMITTED("omitted")

class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant

class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant

Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

SUMMARIZED("summarized")

OMITTED("omitted")

class BetaThinkingDelta:

String thinking

JsonValue; type "thinking\_delta"constant"thinking\_delta"constant

class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value

class BetaTokenTaskBudget:

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

class BetaTool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Boolean> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Type> type

class BetaToolBash20241022:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20241022"constant"bash\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolChoice: A class that can be one of several variants.union

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant

Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20241022"constant"computer\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20250124"constant"computer\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20251124"constant"computer\_20251124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<Boolean> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock:

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Content> content

Accepts one of the following:

String

List<Block>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaSearchResultBlockParam:

List<[BetaTextBlockParam](api/beta.md)> content

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

class BetaRequestDocumentBlock:

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError

class BetaToolSearchToolBm25\_20251119:

JsonValue; name "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonValue; name "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaToolSearchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

List<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolResultErrorParam:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

class BetaToolSearchToolSearchResultBlockParam:

List<[BetaToolReferenceBlockParam](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

class BetaToolTextEditor20241022:

JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20241022"constant"text\_editor\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolUnion: A class that can be one of several variants.union

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

class BetaTool:

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required

String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Boolean> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Type> type

class BetaToolBash20241022:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20241022"constant"bash\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250522"constant"code\_execution\_20250522"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20241022"constant"computer\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory\_20250818"constant"memory\_20250818"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20250124"constant"computer\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20241022"constant"text\_editor\_20241022"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.

JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20251124"constant"computer\_20251124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<Boolean> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<[BetaUserLocation](api/beta.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20250910:

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20260209:

JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260209"constant"web\_search\_20260209"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<[BetaUserLocation](api/beta.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20260209:

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260209"constant"web\_fetch\_20260209"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260309"constant"web\_fetch\_20260309"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaAdvisorTool20260301:

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; name "advisor"constant"advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "advisor\_20260301"constant"advisor\_20260301"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCacheControlEphemeral](api/beta.md)> caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25\_20251119:

JsonValue; name "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonValue; name "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

Accepts one of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp\_toolset"constant"mcp\_toolset"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Configs> configs

Configuration overrides for specific tools, keyed by tool name

Optional<Boolean> deferLoading

Optional<Boolean> enabled

Optional<[BetaMcpToolDefaultConfig](api/beta.md)> defaultConfig

Default configuration applied to all tools from this server

Optional<Boolean> deferLoading

Optional<Boolean> enabled

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaToolUsesKeep:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaUsage:

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaUserLocation:

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](api/beta.md) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910:

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260209:

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260209"constant"web\_fetch\_20260209"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.

JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260309"constant"web\_fetch\_20260309"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlockParam:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

[BetaRequestDocumentBlock](api/beta.md) content

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

class BetaContentBlockSource:

Content content

Accepts one of the following:

String

List<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<List<[BetaTextCitationParam](api/beta.md)>> citations

Accepts one of the following:

class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocationParam:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

class BetaImageBlockParam:

Source source

Accepts one of the following:

class BetaBase64ImageSource:

String data

MediaType mediaType

Accepts one of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant

class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant

class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url

class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<[BetaCitationsConfigParam](api/beta.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchToolResultErrorBlockParam:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

enum BetaWebFetchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

class BetaWebSearchResultBlock:

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

class BetaWebSearchResultBlockParam:

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge

class BetaWebSearchTool20250305:

JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<[BetaUserLocation](api/beta.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchTool20260209:

JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260209"constant"web\_search\_20260209"constant

Optional<List<AllowedCaller>> allowedCallers

Accepts one of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<[BetaUserLocation](api/beta.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchToolRequestError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockContent: A class that can be one of several variants.union

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

class BetaWebSearchToolResultBlockParam:

[BetaWebSearchToolResultBlockParamContent](api/beta.md) content

Accepts one of the following:

List<[BetaWebSearchResultBlockParam](api/beta.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge

class BetaWebSearchToolRequestError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<[BetaCacheControlEphemeral](api/beta.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant

Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlockParamContent: A class that can be one of several variants.union

List<[BetaWebSearchResultBlockParam](api/beta.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge

class BetaWebSearchToolRequestError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

enum BetaWebSearchToolResultErrorCode:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

BatchListPage beta().messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

[BetaMessageBatch](api/beta.md) beta().messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

[BetaDeletedMessageBatch](api/beta.md) beta().messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

[BetaMessageBatchIndividualResponse](api/beta.md) beta().messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message\_batch\_deleted"constant"message\_batch\_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch:

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<LocalDateTime> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

Optional<LocalDateTime> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

Optional<LocalDateTime> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

Accepts one of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")

[BetaMessageBatchRequestCounts](api/beta.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

Optional<String> resultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonValue; type "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchIndividualResponse:

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[BetaMessageBatchResult](api/beta.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchRequestCounts:

long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.

long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

class BetaMessageBatchResult: A class that can be one of several variants.union

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

class BetaMessageBatchErroredResult:

[BetaErrorResponse](api/beta.md) error

[BetaError](api/beta.md) error

Accepts one of the following:

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

Optional<String> requestId

JsonValue; type "error"constant"error"constant

JsonValue; type "errored"constant"errored"constant

class BetaMessageBatchCanceledResult:

JsonValue; type "canceled"constant"canceled"constant

class BetaMessageBatchExpiredResult:

JsonValue; type "expired"constant"expired"constant

class BetaMessageBatchSucceededResult:

[BetaMessage](api/beta.md) message

String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<[BetaContainer](api/beta.md)> container

Information about the container used in the request (for the code execution tool)

String id

Identifier for the container used in this request

LocalDateTime expiresAt

The time at which the container will expire.

Optional<List<[BetaSkill](api/beta.md)>> skills

Skills loaded in the container

String skillId

Skill ID

Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

String version

Skill version or 'latest' for most recent version

List<[BetaContentBlock](api/beta.md)> content

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

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

class BetaThinkingBlock:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant

class BetaRedactedThinkingBlock:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant

class BetaToolUseBlock:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaServerToolUseBlock:

String id

Input input

Name name

Accepts one of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebSearchToolResultBlock:

[BetaWebSearchToolResultBlockContent](api/beta.md) content

Accepts one of the following:

class BetaWebSearchToolResultError:

[BetaWebSearchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

List<[BetaWebSearchResultBlock](api/beta.md)>

String encryptedContent

Optional<String> pageAge

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaWebFetchToolResultBlock:

Content content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock:

[BetaWebFetchToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlock:

[BetaDocumentBlock](api/beta.md) content

Optional<[BetaCitationConfig](api/beta.md)> citations

Citation configuration for the document

boolean enabled

Source source

Accepts one of the following:

class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant

class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant

Optional<String> title

The title of the document

JsonValue; type "document"constant"document"constant

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant

Optional<Caller> caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant

class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant

class BetaAdvisorToolResultBlock:

Content content

Accepts one of the following:

class BetaAdvisorToolResultError:

ErrorCode errorCode

Accepts one of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant

class BetaAdvisorResultBlock:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

class BetaAdvisorRedactedResultBlock:

String encryptedContent

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant

class BetaCodeExecutionToolResultBlock:

[BetaCodeExecutionToolResultBlockContent](api/beta.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError:

[BetaCodeExecutionToolResultErrorCode](api/beta.md) errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlock:

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant

class BetaEncryptedCodeExecutionResultBlock:

Code execution result with encrypted stdout for PFC + web\_search results.

List<[BetaCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant

class BetaBashCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlock:

List<[BetaBashCodeExecutionOutputBlock](api/beta.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant

class BetaTextEditorCodeExecutionToolResultBlock:

Content content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

Optional<String> errorMessage

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

class BetaTextEditorCodeExecutionViewResultBlock:

String content

FileType fileType

Accepts one of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

class BetaTextEditorCodeExecutionCreateResultBlock:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlock:

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant

class BetaToolSearchToolResultBlock:

Content content

Accepts one of the following:

class BetaToolSearchToolResultError:

ErrorCode errorCode

Accepts one of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

Optional<String> errorMessage

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlock:

List<[BetaToolReferenceBlock](api/beta.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant

class BetaMcpToolUseBlock:

String id

Input input

String name

The name of the MCP tool

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant

class BetaMcpToolResultBlock:

Content content

Accepts one of the following:

String

List<[BetaTextBlock](api/beta.md)>

Optional<List<[BetaTextCitation](api/beta.md)>> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

Optional<String> fileId

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant

class BetaCitationPageLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

Optional<String> fileId

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant

class BetaCitationContentBlockLocation:

String citedText

long documentIndex

Optional<String> documentTitle

long endBlockIndex

Optional<String> fileId

long startBlockIndex

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant

class BetaCitationsWebSearchResultLocation:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url

class BetaCitationSearchResultLocation:

String citedText

long endBlockIndex

long searchResultIndex

String source

long startBlockIndex

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String text

JsonValue; type "text"constant"text"constant

boolean isError

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant

class BetaContainerUploadBlock:

Response model for a file uploaded to the container.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant

class BetaCompactionBlock:

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

Optional<String> content

Summary of compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim

JsonValue; type "compaction"constant"compaction"constant

Optional<[BetaContextManagementResponse](api/beta.md)> contextManagement

Context management response.

Information about context management strategies applied during the request.

List<AppliedEdit> appliedEdits

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedToolUses

Number of tool uses that were cleared.

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant

The type of context management edit applied.

class BetaClearThinking20251015EditResponse:

long clearedInputTokens

Number of input tokens cleared by this edit.

long clearedThinkingTurns

Number of thinking turns that were cleared.

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant

The type of context management edit applied.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

JsonValue; role "assistant"constant"assistant"constant

Conversational role of the generated message.

This will always be `"assistant"`.

Optional<[BetaRefusalStopDetails](api/beta.md)> stopDetails

Structured information about a refusal.

Optional<Category> category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

CYBER("cyber")

BIO("bio")

Optional<String> explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

JsonValue; type "refusal"constant"refusal"constant

Optional<[BetaStopReason](api/beta.md)> stopReason

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

COMPACTION("compaction")

REFUSAL("refusal")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED("model\_context\_window\_exceeded")

Optional<String> stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

JsonValue; type "message"constant"message"constant

Object type.

For Messages, this is always `"message"`.

[BetaUsage](api/beta.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

Optional<Long> cacheCreationInputTokens

The number of input tokens used to create the cache entry.

Optional<Long> cacheReadInputTokens

The number of input tokens read from the cache.

Optional<String> inferenceGeo

The geographic region where inference was performed for this request.

long inputTokens

The number of input tokens which were used.

Optional<List<BetaIterationsUsageItems>> iterations

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage:

Token usage for a sampling iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "message"constant"message"constant

Usage for a sampling iteration

class BetaCompactionIterationUsage:

Token usage for a compaction iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

long outputTokens

The number of output tokens which were used.

JsonValue; type "compaction"constant"compaction"constant

Usage for a compaction iteration

class BetaAdvisorMessageIterationUsage:

Token usage for an advisor sub-inference iteration.

Optional<[BetaCacheCreation](api/beta.md)> cacheCreation

Breakdown of cached tokens by TTL

long ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

long ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

long cacheCreationInputTokens

The number of input tokens used to create the cache entry.

long cacheReadInputTokens

The number of input tokens read from the cache.

long inputTokens

The number of input tokens which were used.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

long outputTokens

The number of output tokens which were used.

JsonValue; type "advisor\_message"constant"advisor\_message"constant

Usage for an advisor sub-inference iteration

long outputTokens

The number of output tokens which were used.

Optional<[BetaServerToolUsage](api/beta.md)> serverToolUse

The number of server tool requests.

long webFetchRequests

The number of web fetch tool requests.

long webSearchRequests

The number of web search tool requests.

Optional<ServiceTier> serviceTier

If the request used the priority, standard, or batch tier.

Accepts one of the following:

STANDARD("standard")

PRIORITY("priority")

BATCH("batch")

Optional<Speed> speed

The inference speed mode used for this request.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

JsonValue; type "succeeded"constant"succeeded"constant

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().create(AgentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

AgentListPage beta().agents().list(AgentListParamsparams = AgentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().retrieve(AgentRetrieveParamsparams = AgentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().update(AgentUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

[BetaManagedAgentsAgent](api/beta.md) beta().agents().archive(AgentArchiveParamsparams = AgentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent:

A Managed Agents `agent`.

String id

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

Optional<String> description

List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url

Metadata metadata

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

String name

List<Skill> skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system

List<Tool> tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

long version

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentToolConfig:

Configuration for a specific agent tool.

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolConfigParams:

Configuration override for a specific tool within a toolset.

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolsetDefaultConfig:

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolsetDefaultConfigParams:

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsAgentToolset20260401Params:

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

Type type

Optional<List<[BetaManagedAgentsAgentToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

Optional<Boolean> enabled

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools in a toolset.

Optional<Boolean> enabled

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

class BetaManagedAgentsCustomToolInputSchema:

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams:

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

String description

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

Type type

class BetaManagedAgentsMcpServerUrlDefinition:

URL-based MCP server connection as returned in API responses.

String name

Type type

String url

class BetaManagedAgentsMcpToolConfig:

Resolved configuration for a specific MCP tool.

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolConfigParams:

Configuration override for a specific MCP tool.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsMcpToolsetDefaultConfig:

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolsetDefaultConfigParams:

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

class BetaManagedAgentsMcpToolsetParams:

Configuration for tools from an MCP server defined in `mcp_servers`.

String mcpServerName

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

Type type

Optional<List<[BetaManagedAgentsMcpToolConfigParams](api/beta.md)>> configs

Per-tool configuration overrides.

String name

Name of the MCP tool to configure. 1-128 characters.

Optional<Boolean> enabled

Whether this tool is enabled. Overrides the `default_config` setting.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Optional<[BetaManagedAgentsMcpToolsetDefaultConfigParams](api/beta.md)> defaultConfig

Default configuration for all tools from an MCP server.

Optional<Boolean> enabled

Whether tools are enabled by default. Defaults to true if not specified.

Optional<PermissionPolicy> permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

enum BetaManagedAgentsModel:

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

class BetaManagedAgentsModelConfig:

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaManagedAgentsModelConfigParams:

An object that defines additional configuration control over model use

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaManagedAgentsSkillParams: A class that can be one of several variants.union

Skill to load in the session container.

class BetaManagedAgentsAnthropicSkillParams:

An Anthropic-managed skill.

String skillId

Identifier of the Anthropic skill (e.g., "xlsx").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams:

A user-created custom skill.

String skillId

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

Type type

Optional<String> version

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsUrlMcpServerParams:

URL-based MCP server connection.

String name

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

Type type

String url

Endpoint URL for the MCP server.

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

VersionListPage beta().agents().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

[BetaEnvironment](api/beta.md) beta().environments().create(EnvironmentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

EnvironmentListPage beta().environments().list(EnvironmentListParamsparams = EnvironmentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

[BetaEnvironment](api/beta.md) beta().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

[BetaEnvironment](api/beta.md) beta().environments().update(EnvironmentUpdateParamsparams = EnvironmentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

[BetaEnvironmentDeleteResponse](api/beta.md) beta().environments().delete(EnvironmentDeleteParamsparams = EnvironmentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

[BetaEnvironment](api/beta.md) beta().environments().archive(EnvironmentArchiveParamsparams = EnvironmentArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig:

`cloud` environment configuration.

Networking networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

[BetaPackages](api/beta.md) packages

Package manager configuration.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

JsonValue; type "cloud"constant"cloud"constant

Environment type

class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "cloud"constant"cloud"constant

Environment type

Optional<Networking> networking

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "limited"constant"limited"constant

Network policy type

Optional<Boolean> allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<Boolean> allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<List<String>> allowedHosts

Specifies domains the container can reach.

Optional<[BetaPackagesParams](api/beta.md)> packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Optional<List<String>> apt

Ubuntu/Debian packages to install

Optional<List<String>> cargo

Rust packages to install

Optional<List<String>> gem

Ruby packages to install

Optional<List<String>> go

Go packages to install

Optional<List<String>> npm

Node.js packages to install

Optional<List<String>> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaEnvironment:

Unified Environment resource for both cloud and BYOC environments.

String id

Environment identifier (e.g., 'env\_...')

Optional<String> archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived

[BetaCloudConfig](api/beta.md) config

`cloud` environment configuration.

Networking networking

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

[BetaPackages](api/beta.md) packages

Package manager configuration.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

JsonValue; type "cloud"constant"cloud"constant

Environment type

String createdAt

RFC 3339 timestamp when environment was created

String description

User-provided description for the environment

Metadata metadata

User-provided metadata key-value pairs

String name

Human-readable name for the environment

JsonValue; type "environment"constant"environment"constant

The type of object (always 'environment')

String updatedAt

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse:

Response after deleting an environment.

String id

Environment identifier

JsonValue; type "environment\_deleted"constant"environment\_deleted"constant

The type of response

class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type

class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "limited"constant"limited"constant

Network policy type

Optional<Boolean> allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<Boolean> allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<List<String>> allowedHosts

Specifies domains the container can reach.

class BetaPackages:

Packages (and their versions) available in this environment.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaPackagesParams:

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Optional<List<String>> apt

Ubuntu/Debian packages to install

Optional<List<String>> cargo

Rust packages to install

Optional<List<String>> gem

Ruby packages to install

Optional<List<String>> go

Go packages to install

Optional<List<String>> npm

Node.js packages to install

Optional<List<String>> pip

Python packages to install

Optional<Type> type

Package configuration type

class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type

#### BetaSessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

SessionListPage beta().sessions().list(SessionListParamsparams = SessionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().retrieve(SessionRetrieveParamsparams = SessionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().update(SessionUpdateParamsparams = SessionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta.md) beta().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta.md) beta().sessions().archive(SessionArchiveParamsparams = SessionArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

String id

The `agent` ID.

Type type

Optional<Long> version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCacheCreationUsage:

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsDeletedSession:

Confirmation that a `session` has been permanently deleted.

String id

Type type

class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

String fileId

ID of a previously uploaded file.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

String authorizationToken

GitHub authorization token used to clone the repository.

Type type

String url

Github URL of the repository

Optional<Checkout> checkout

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

Optional<String> mountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsSession:

A Managed Agents `session`.

String id

[BetaManagedAgentsSessionAgent](api/beta.md) agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description

List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

String name

List<Skill> skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system

List<Tool> tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

Type type

long version

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

String environmentId

Metadata metadata

List<[BetaManagedAgentsSessionResource](api/beta.md)> resources

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url

Optional<Checkout> checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsSessionStats](api/beta.md) stats

Timing statistics for a session.

Optional<Double> activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

Status status

SessionStatus enum

Accepts one of the following:

RESCHEDULING("rescheduling")

RUNNING("running")

IDLE("idle")

TERMINATED("terminated")

Optional<String> title

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

[BetaManagedAgentsSessionUsage](api/beta.md) usage

Cumulative token usage for a session across all turns.

Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.

List<String> vaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

class BetaManagedAgentsSessionAgent:

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

String id

Optional<String> description

List<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> mcpServers

String name

Type type

String url

[BetaManagedAgentsModelConfig](api/beta.md) model

Model identifier and configuration.

BetaManagedAgentsModel id

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

String name

List<Skill> skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

String skillId

Type type

String version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

String skillId

Type type

String version

Optional<String> system

List<Tool> tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

List<[BetaManagedAgentsAgentToolConfig](api/beta.md)> configs

boolean enabled

Name name

Built-in agent tool identifier.

Accepts one of the following:

BASH("bash")

EDIT("edit")

READ("read")

WRITE("write")

GLOB("glob")

GREP("grep")

WEB\_FETCH("web\_fetch")

WEB\_SEARCH("web\_search")

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for agent tools.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

Type type

class BetaManagedAgentsMcpToolset:

List<[BetaManagedAgentsMcpToolConfig](api/beta.md)> configs

boolean enabled

String name

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

[BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) defaultConfig

Resolved default configuration for all tools from an MCP server.

boolean enabled

PermissionPolicy permissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

Type type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

Type type

String mcpServerName

Type type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

String description

[BetaManagedAgentsCustomToolInputSchema](api/beta.md) inputSchema

JSON Schema for custom tool input parameters.

Optional<Properties> properties

JSON Schema properties defining the tool's input parameters.

Optional<List<String>> required

List of required property names.

Optional<Type> type

Must be 'object' for tool input schemas.

String name

Type type

Type type

long version

class BetaManagedAgentsSessionStats:

Timing statistics for a session.

Optional<Double> activeSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Optional<Double> durationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

class BetaManagedAgentsSessionUsage:

Cumulative token usage for a session across all turns.

Optional<[BetaManagedAgentsCacheCreationUsage](api/beta.md)> cacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Optional<Long> ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Optional<Long> ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Optional<Long> cacheReadInputTokens

Total tokens read from prompt cache.

Optional<Long> inputTokens

Total input tokens consumed across all turns.

Optional<Long> outputTokens

Total output tokens generated across all turns.

#### BetaSessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta.md) beta().sessions().events().send(EventSendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta.md) beta().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.

List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

class BetaManagedAgentsEventParams: A class that can be one of several variants.union

Union type for event parameters that can be sent to a session.

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

List<Content> content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

Type type

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.

Optional<List<Data>> data

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.

List<Content> content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union

Union type for all event types in a session.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.

List<Content> content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.

List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.

[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.

[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelUsage:

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union

Server-sent event in the session stream.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.

List<Content> content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the custom tool being called.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

String id

Unique identifier for this event.

List<[BetaManagedAgentsTextBlock](api/beta.md)> content

Array of text blocks comprising the agent response.

String text

The text content.

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String mcpServerName

Name of the MCP server providing the tool.

String name

Name of the MCP tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

String id

Unique identifier for this event.

String mcpToolUseId

The id of the `agent.mcp_tool_use` event this result corresponds to.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

String id

Unique identifier for this event.

Input input

Input parameters for the tool call.

String name

Name of the agent tool being used.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

Optional<EvaluatedPermission> evaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

ALLOW("allow")

ASK("ask")

DENY("deny")

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

String toolUseId

The id of the `agent.tool_use` event this result corresponds to.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

String id

Unique identifier for this event.

Error error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

String mcpServerName

Name of the MCP server that failed to connect.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

String mcpServerName

Name of the MCP server that failed authentication.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

StopReason stopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

Type type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

List<String> eventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type type

Type type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

String id

Unique identifier for this event.

Optional<Boolean> isError

Whether the model request resulted in an error.

String modelRequestStartId

The id of the corresponding `span.model_request_start` event.

[BetaManagedAgentsSpanModelUsage](api/beta.md) modelUsage

Token usage for a single model request.

long cacheCreationInputTokens

Tokens used to create prompt cache in this request.

long cacheReadInputTokens

Tokens read from prompt cache in this request.

long inputTokens

Input tokens consumed by this request.

long outputTokens

Output tokens generated by this request.

Optional<Speed> speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

STANDARD("standard")

FAST("fast")

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

String id

Unique identifier for this event.

LocalDateTime processedAt

A timestamp in RFC 3339 format

Type type

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

String message

Human-readable error description.

RetryStatus retryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

Type type

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

String id

Unique identifier for this event.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

String customToolUseId

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<List<Content>> content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Optional<Boolean> isError

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

String id

Unique identifier for this event.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

Type type

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

String id

Unique identifier for this event.

List<Content> content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

List<Content> content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

String text

The text content.

Type type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

Source source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

String data

Base64-encoded image data.

String mediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

Type type

String url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

String data

Base64-encoded document data.

String mediaType

MIME type of the document (e.g., "application/pdf").

Type type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

String data

The plain text content.

MediaType mediaType

MIME type of the text content. Must be "text/plain".

Type type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

Type type

String url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

String fileId

ID of a previously uploaded file.

Type type

Type type

Optional<String> context

Additional context about the document for the model.

Optional<String> title

The title of the document.

Type type

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

String id

Unique identifier for this event.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

Optional<LocalDateTime> processedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

Result result

UserToolConfirmationResult enum

Accepts one of the following:

ALLOW("allow")

DENY("deny")

String toolUseId

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type type

Optional<String> denyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### BetaSessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) beta().sessions().resources().add(ResourceAddParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

ResourceListPage beta().sessions().resources().list(ResourceListParamsparams = ResourceListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) beta().sessions().resources().retrieve(ResourceRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) beta().sessions().resources().update(ResourceUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) beta().sessions().resources().delete(ResourceDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

String id

Type type

class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url

Optional<Checkout> checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsSessionResource: A class that can be one of several variants.union

class BetaManagedAgentsGitHubRepositoryResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String url

Optional<Checkout> checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

String name

Branch name to check out.

Type type

class BetaManagedAgentsCommitCheckout:

String sha

Full commit SHA to check out.

Type type

class BetaManagedAgentsFileResource:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String fileId

String mountPath

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().create(VaultCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

VaultListPage beta().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta.md) beta().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().archive(VaultArchiveParamsparams = VaultArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault:

Confirmation of a deleted vault.

String id

Unique identifier of the deleted vault.

Type type

class BetaManagedAgentsVault:

A vault that stores credentials for use by agents during sessions.

String id

Unique identifier for the vault.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

String displayName

Human-readable name for the vault.

Metadata metadata

Arbitrary key-value metadata attached to the vault.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

CredentialListPage beta().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta.md) beta().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

String id

Unique identifier for the credential.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

Auth auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata attached to the credential.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault this credential belongs to.

Optional<String> displayName

Human-readable name for the credential.

class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

String id

Unique identifier of the deleted credential.

Type type

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

String accessToken

OAuth access token.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)> refresh

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.

Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

Type type

Optional<String> accessToken

Updated OAuth access token.

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta.md)> refresh

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.

Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

String token

Static bearer token value.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

Type type

Optional<String> token

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta.md) beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/files

##### [List Files](api/beta/files/list.md)

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta.md) beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta.md) beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class BetaFileScope:

String id

The ID of the scoping resource (e.g., the session ID).

JsonValue; type "session"constant"session"constant

The type of scope (e.g., `"session"`).

class DeletedFile:

String id

ID of the deleted file.

Optional<Type> type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

String id

Unique object identifier.

The format and length of IDs may change over time.

LocalDateTime createdAt

RFC 3339 datetime string representing when the file was created.

String filename

Original filename of the uploaded file.

String mimeType

MIME type of the file.

long sizeBytes

Size of the file in bytes.

JsonValue; type "file"constant"file"constant

Object type.

For files, this is always `"file"`.

Optional<Boolean> downloadable

Whether the file can be downloaded.

Optional<[BetaFileScope](api/beta.md)> scope

The scope of this file, indicating the context in which it was created (e.g., a session).

String id

The ID of the scoping resource (e.g., the session ID).

JsonValue; type "session"constant"session"constant

The type of scope (e.g., `"session"`).

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

[SkillCreateResponse](api/beta.md) beta().skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

SkillListPage beta().skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

[SkillRetrieveResponse](api/beta.md) beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

[SkillDeleteResponse](api/beta.md) beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

[VersionCreateResponse](api/beta.md) beta().skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

[VersionRetrieveResponse](api/beta.md) beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

[VersionDeleteResponse](api/beta.md) beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill\_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().create(UserProfileCreateParamsparams = UserProfileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

UserProfileListPage beta().userProfiles().list(UserProfileListParamsparams = UserProfileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().retrieve(UserProfileRetrieveParamsparams = UserProfileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta.md) beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile:

String id

Unique identifier for this user profile, prefixed `uprof_`.

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

TrustGrants trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Status status

Status of the trust grant.

Accepts one of the following:

ACTIVE("active")

PENDING("pending")

REJECTED("rejected")

Type type

Object type. Always `user_profile`.

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> externalId

Platform's own identifier for this user. Not enforced unique.

class BetaUserProfileEnrollmentUrl:

LocalDateTime expiresAt

A timestamp in RFC 3339 format

Type type

Object type. Always `enrollment_url`.

String url

Enrollment URL to send to the end user. Valid until `expires_at`.

class BetaUserProfileTrustGrant:

Status status

Status of the trust grant.

Accepts one of the following:

ACTIVE("active")

PENDING("pending")

REJECTED("rejected")

---

*Copyright © Anthropic. All rights reserved.*
