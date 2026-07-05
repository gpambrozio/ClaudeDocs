# Create a Message Batch

Copy page



Java

# Create a Message Batch

[BetaMessageBatch](api/beta/messages/batches.md) beta().messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](build-with-claude/batch-processing.md)

##### ParametersExpand Collapse



BatchCreateParams params



Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")

Optional<String> userProfileId

The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.



List<Request> requests

List of requests for prompt completion. Each is an individual request to create a Message.



String customId

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1



Params params

Messages API creation parameters for the individual request.

See the [Messages API reference](api/messages.md) for full documentation on available parameters.



long maxTokens

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](build-with-claude/prompt-caching.md) without generating a response.

Different models have different maximum values for this parameter. See [models](about-claude/models/overview.md) for details.

minimum0



List<[BetaMessageParam](api/beta/messages.md)> messages

Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```shiki
[{"role": "user", "content": "Hello, Claude"}]
```



Example with multiple conversational turns:

```shiki
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```



Example with a partially-filled response from Claude:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```



Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```shiki
{"role": "user", "content": "Hello, Claude"}
```



```shiki
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```



See [input examples](build-with-claude/working-with-messages.md).

Note that if you want to include a [system prompt](build-with-claude/prompt-engineering/claude-prompting-best-practices.md), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



Content content

One of the following:

String



List<[BetaContentBlockParam](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaThinkingBlockParam:

String signature

String thinking

JsonValue; type "thinking"constant"thinking"constant



class BetaRedactedThinkingBlockParam:

String data

JsonValue; type "redacted\_thinking"constant"redacted\_thinking"constant



class BetaToolUseBlockParam:

String id

Input input

String name

JsonValue; type "tool\_use"constant"tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaToolResultBlockParam:

String toolUseId

JsonValue; type "tool\_result"constant"tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<Block>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaSearchResultBlockParam:



List<[BetaTextBlockParam](api/beta/messages.md)> content

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

String source

String title

JsonValue; type "search\_result"constant"search\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled



class BetaRequestDocumentBlock:



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> isError



class BetaServerToolUseBlockParam:

String id

Input input



Name name

One of the following:

ADVISOR("advisor")

WEB\_SEARCH("web\_search")

WEB\_FETCH("web\_fetch")

CODE\_EXECUTION("code\_execution")

BASH\_CODE\_EXECUTION("bash\_code\_execution")

TEXT\_EDITOR\_CODE\_EXECUTION("text\_editor\_code\_execution")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")

JsonValue; type "server\_tool\_use"constant"server\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockParam:



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md) content

One of the following:



List<[BetaWebSearchResultBlockParam](api/beta/messages.md)>

String encryptedContent

String title

JsonValue; type "web\_search\_result"constant"web\_search\_result"constant

String url

Optional<String> pageAge



class BetaWebSearchToolRequestError:



[BetaWebSearchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

TOO\_MANY\_REQUESTS("too\_many\_requests")

QUERY\_TOO\_LONG("query\_too\_long")

REQUEST\_TOO\_LARGE("request\_too\_large")

JsonValue; type "web\_search\_tool\_result\_error"constant"web\_search\_tool\_result\_error"constant

String toolUseId

JsonValue; type "web\_search\_tool\_result"constant"web\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaWebFetchToolResultBlockParam:



Content content

One of the following:



class BetaWebFetchToolResultErrorBlockParam:



[BetaWebFetchToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

URL\_TOO\_LONG("url\_too\_long")

URL\_NOT\_ALLOWED("url\_not\_allowed")

URL\_NOT\_IN\_PRIOR\_CONTEXT("url\_not\_in\_prior\_context")

URL\_NOT\_ACCESSIBLE("url\_not\_accessible")

UNSUPPORTED\_CONTENT\_TYPE("unsupported\_content\_type")

TOO\_MANY\_REQUESTS("too\_many\_requests")

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

UNAVAILABLE("unavailable")

JsonValue; type "web\_fetch\_tool\_result\_error"constant"web\_fetch\_tool\_result\_error"constant



class BetaWebFetchBlockParam:



[BetaRequestDocumentBlock](api/beta/messages.md) content



Source source

One of the following:



class BetaBase64PdfSource:

String data

JsonValue; mediaType "application/pdf"constant"application/pdf"constant

JsonValue; type "base64"constant"base64"constant



class BetaPlainTextSource:

String data

JsonValue; mediaType "text/plain"constant"text/plain"constant

JsonValue; type "text"constant"text"constant



class BetaContentBlockSource:



Content content

One of the following:

String



List<[BetaContentBlockSourceContent](api/beta/messages.md)>

One of the following:



class BetaTextBlockParam:

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



class BetaImageBlockParam:



Source source

One of the following:



class BetaBase64ImageSource:

String data



MediaType mediaType

One of the following:

IMAGE\_JPEG("image/jpeg")

IMAGE\_PNG("image/png")

IMAGE\_GIF("image/gif")

IMAGE\_WEBP("image/webp")

JsonValue; type "base64"constant"base64"constant



class BetaUrlImageSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileImageSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "image"constant"image"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "content"constant"content"constant



class BetaUrlPdfSource:

JsonValue; type "url"constant"url"constant

String url



class BetaFileDocumentSource:

String fileId

JsonValue; type "file"constant"file"constant

JsonValue; type "document"constant"document"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Optional<Boolean> enabled

Optional<String> context

Optional<String> title

JsonValue; type "web\_fetch\_result"constant"web\_fetch\_result"constant

String url

Fetched content URL

Optional<String> retrievedAt

ISO 8601 timestamp when the content was retrieved

String toolUseId

JsonValue; type "web\_fetch\_tool\_result"constant"web\_fetch\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Caller> caller

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller:

Tool invocation directly from the model.

JsonValue; type "direct"constant"direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

String toolId

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

String toolId

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



class BetaAdvisorToolResultBlockParam:



Content content

One of the following:



class BetaAdvisorToolResultErrorParam:



ErrorCode errorCode

One of the following:

MAX\_USES\_EXCEEDED("max\_uses\_exceeded")

PROMPT\_TOO\_LONG("prompt\_too\_long")

TOO\_MANY\_REQUESTS("too\_many\_requests")

OVERLOADED("overloaded")

UNAVAILABLE("unavailable")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

MODEL\_NOT\_FOUND("model\_not\_found")

JsonValue; type "advisor\_tool\_result\_error"constant"advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlockParam:

String text

JsonValue; type "advisor\_result"constant"advisor\_result"constant

Optional<String> stopReason



class BetaAdvisorRedactedResultBlockParam:

String encryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonValue; type "advisor\_redacted\_result"constant"advisor\_redacted\_result"constant

Optional<String> stopReason

String toolUseId

JsonValue; type "advisor\_tool\_result"constant"advisor\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCodeExecutionToolResultBlockParam:



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam:



[BetaCodeExecutionToolResultErrorCode](api/beta/messages.md) errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "code\_execution\_tool\_result\_error"constant"code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "code\_execution\_result"constant"code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



List<[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "code\_execution\_output"constant"code\_execution\_output"constant

String encryptedStdout

long returnCode

String stderr

JsonValue; type "encrypted\_code\_execution\_result"constant"encrypted\_code\_execution\_result"constant

String toolUseId

JsonValue; type "code\_execution\_tool\_result"constant"code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaBashCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

OUTPUT\_FILE\_TOO\_LARGE("output\_file\_too\_large")

JsonValue; type "bash\_code\_execution\_tool\_result\_error"constant"bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlockParam:



List<[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)> content

String fileId

JsonValue; type "bash\_code\_execution\_output"constant"bash\_code\_execution\_output"constant

long returnCode

String stderr

String stdout

JsonValue; type "bash\_code\_execution\_result"constant"bash\_code\_execution\_result"constant

String toolUseId

JsonValue; type "bash\_code\_execution\_tool\_result"constant"bash\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaTextEditorCodeExecutionToolResultBlockParam:



Content content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

FILE\_NOT\_FOUND("file\_not\_found")

JsonValue; type "text\_editor\_code\_execution\_tool\_result\_error"constant"text\_editor\_code\_execution\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaTextEditorCodeExecutionViewResultBlockParam:

String content



FileType fileType

One of the following:

TEXT("text")

IMAGE("image")

PDF("pdf")

JsonValue; type "text\_editor\_code\_execution\_view\_result"constant"text\_editor\_code\_execution\_view\_result"constant

Optional<Long> numLines

Optional<Long> startLine

Optional<Long> totalLines



class BetaTextEditorCodeExecutionCreateResultBlockParam:

boolean isFileUpdate

JsonValue; type "text\_editor\_code\_execution\_create\_result"constant"text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonValue; type "text\_editor\_code\_execution\_str\_replace\_result"constant"text\_editor\_code\_execution\_str\_replace\_result"constant

Optional<List<String>> lines

Optional<Long> newLines

Optional<Long> newStart

Optional<Long> oldLines

Optional<Long> oldStart

String toolUseId

JsonValue; type "text\_editor\_code\_execution\_tool\_result"constant"text\_editor\_code\_execution\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaToolSearchToolResultBlockParam:



Content content

One of the following:



class BetaToolSearchToolResultErrorParam:



ErrorCode errorCode

One of the following:

INVALID\_TOOL\_INPUT("invalid\_tool\_input")

UNAVAILABLE("unavailable")

TOO\_MANY\_REQUESTS("too\_many\_requests")

EXECUTION\_TIME\_EXCEEDED("execution\_time\_exceeded")

JsonValue; type "tool\_search\_tool\_result\_error"constant"tool\_search\_tool\_result\_error"constant

Optional<String> errorMessage



class BetaToolSearchToolSearchResultBlockParam:



List<[BetaToolReferenceBlockParam](api/beta/messages.md)> toolReferences

String toolName

JsonValue; type "tool\_reference"constant"tool\_reference"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

JsonValue; type "tool\_search\_tool\_search\_result"constant"tool\_search\_tool\_search\_result"constant

String toolUseId

JsonValue; type "tool\_search\_tool\_result"constant"tool\_search\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaMcpToolUseBlockParam:

String id

Input input

String name

String serverName

The name of the MCP server

JsonValue; type "mcp\_tool\_use"constant"mcp\_tool\_use"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaRequestMcpToolResultBlockParam:

String toolUseId

JsonValue; type "mcp\_tool\_result"constant"mcp\_tool\_result"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Content> content

One of the following:

String



List<[BetaTextBlockParam](api/beta/messages.md)>

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

Optional<Boolean> isError



class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

String fileId

JsonValue; type "container\_upload"constant"container\_upload"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

JsonValue; type "compaction"constant"compaction"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<String> content

Summary of previously compacted content, or null if compaction failed

Optional<String> encryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



List<[BetaTextBlockParam](api/beta/messages.md)> content

System instruction text blocks.

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant

JsonValue; type "mid\_conv\_system"constant"mid\_conv\_system"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



class BetaFallbackBlockParam:

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

[BetaFallbackInfoParam](api/beta/messages.md) from

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



[BetaFallbackInfoParam](api/beta/messages.md) to

Identifies one hop of a fallback transition.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

JsonValue; type "fallback"constant"fallback"constant

Optional<JsonValue> trigger

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



Role role

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Container> container

Container identifier for reuse across requests.

One of the following:



class BetaContainerParams:

Container parameters with skills to be loaded.

Optional<String> id

Container id



Optional<List<[BetaSkillParams](api/beta/messages.md)>> skills

List of skills to load in the container

String skillId

Skill ID



Type type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

ANTHROPIC("anthropic")

CUSTOM("custom")

Optional<String> version

Skill version or 'latest' for most recent version

String



Optional<[BetaContextManagementConfig](api/beta/messages.md)> contextManagement

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



Optional<List<Edit>> edits

List of context management edits to apply

One of the following:



class BetaClearToolUses20250919Edit:

JsonValue; type "clear\_tool\_uses\_20250919"constant"clear\_tool\_uses\_20250919"constant



Optional<[BetaInputTokensClearAtLeast](api/beta/messages.md)> clearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



Optional<ClearToolInputs> clearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

boolean

List<String>

Optional<List<String>> excludeTools

Tool names whose uses are preserved from clearing



Optional<[BetaToolUsesKeep](api/beta/messages.md)> keep

Number of tool uses to retain in the conversation

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



Optional<Trigger> trigger

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger:

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



class BetaToolUsesTrigger:

JsonValue; type "tool\_uses"constant"tool\_uses"constant

long value



class BetaClearThinking20251015Edit:

JsonValue; type "clear\_thinking\_20251015"constant"clear\_thinking\_20251015"constant



Optional<Keep> keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns:

JsonValue; type "thinking\_turns"constant"thinking\_turns"constant

long value



class BetaAllThinkingTurns:

JsonValue; type "all"constant"all"constant

JsonValue;



class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonValue; type "compact\_20260112"constant"compact\_20260112"constant

Optional<String> instructions

Additional instructions for summarization.

Optional<Boolean> pauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.



Optional<[BetaInputTokensTrigger](api/beta/messages.md)> trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonValue; type "input\_tokens"constant"input\_tokens"constant

long value



Optional<[BetaDiagnosticsParam](api/beta/messages.md)> diagnostics

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

Optional<String> previousMessageId

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



Optional<String> fallbackCreditToken

The `fallback_credit_token` from a prior refusal's `stop_details`.

When a preceding request was refused and returned a `fallback_credit_token`,
pass that code here on the retry to have the retry's cache-creation tokens
for the prefix that was warm on the refused model billed at the cache-read
rate. Must be redeemed by the same organization and workspace, with the same
request body (optionally extended by one appended `assistant` message whose
content is the partial text — with any trailing whitespace stripped from
the final text block — and paired server-tool blocks streamed before the
refusal; the appended-assistant form is not available for requests with
`output_format` set or forced `tool_choice`), on an eligible fallback
model, on the same platform,
and within 5 minutes of the refusal; a mismatch is a 400. A token minted
mid-server-tool-loop whose partial content was continuable may only be
redeemed with the appended-assistant form — if an exact-body retry is
rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry with the appended-assistant form instead.

When the appended-assistant form is used on a model that otherwise disallows
assistant-turn prefill, this token also authorizes that one prefill.

maxLength2048

minLength1



Optional<List<[BetaFallbackParam](api/beta/messages.md)>> fallbacks

Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

Optional<Long> maxTokens



Optional<[BetaOutputConfig](api/beta/messages.md)> outputConfig



Optional<Effort> effort

All possible effort levels.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")



Optional<[BetaJsonOutputFormat](api/beta/messages.md)> format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



Optional<[BetaTokenTaskBudget](api/beta/messages.md)> taskBudget

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



Optional<Speed> speed

One of the following:

STANDARD("standard")

FAST("fast")



Optional<Thinking> thinking

One of the following:



class BetaThinkingConfigEnabled:



long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant



class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")

Optional<String> inferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



Optional<List<[BetaRequestMcpServerUrlDefinition](api/beta/messages.md)>> mcpServers

MCP servers to be utilized in this request

String name

JsonValue; type "url"constant"url"constant

String url

Optional<String> authorizationToken



Optional<[BetaRequestMcpServerToolConfiguration](api/beta/messages.md)> toolConfiguration

Optional<List<String>> allowedTools

Optional<Boolean> enabled



Optional<[BetaMetadata](api/beta/messages.md)> metadata

An object describing metadata about the request.



Optional<String> userId

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



Optional<[BetaOutputConfig](api/beta/messages.md)> outputConfig

Configuration options for the model's output, such as the output format.



Optional<Effort> effort

All possible effort levels.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

MAX("max")



Optional<[BetaJsonOutputFormat](api/beta/messages.md)> format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



Optional<[BetaTokenTaskBudget](api/beta/messages.md)> taskBudget

User-configurable total token budget across contexts.

long total

Total token budget across all contexts in the session.

JsonValue; type "tokens"constant"tokens"constant

The budget type. Currently only 'tokens' is supported.

Optional<Long> remaining

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



DeprecatedOptional<[BetaJsonOutputFormat](api/beta/messages.md)> outputFormat

Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

Schema schema

The JSON schema of the format

JsonValue; type "json\_schema"constant"json\_schema"constant



Optional<ServiceTier> serviceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](api/service-tiers.md) for details.

One of the following:

AUTO("auto")

STANDARD\_ONLY("standard\_only")



Optional<Speed> speed

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

One of the following:

STANDARD("standard")

FAST("fast")



Optional<List<String>> stopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



Optional<Boolean> stream

Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



Optional<System> system

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).

One of the following:

String



List<[BetaTextBlockParam](api/beta/messages.md)>

String text

JsonValue; type "text"constant"text"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<List<[BetaTextCitationParam](api/beta/messages.md)>> citations

One of the following:



class BetaCitationCharLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endCharIndex

long startCharIndex

JsonValue; type "char\_location"constant"char\_location"constant



class BetaCitationPageLocationParam:

String citedText

long documentIndex

Optional<String> documentTitle

long endPageNumber

long startPageNumber

JsonValue; type "page\_location"constant"page\_location"constant



class BetaCitationContentBlockLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

long documentIndex

Optional<String> documentTitle



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonValue; type "content\_block\_location"constant"content\_block\_location"constant



class BetaCitationWebSearchResultLocationParam:

String citedText

String encryptedIndex

Optional<String> title

JsonValue; type "web\_search\_result\_location"constant"web\_search\_result\_location"constant

String url



class BetaCitationSearchResultLocationParam:



String citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



long endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



long searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

String source

long startBlockIndex

0-based index of the first cited block in the source's `content` array.

Optional<String> title

JsonValue; type "search\_result\_location"constant"search\_result\_location"constant



DeprecatedOptional<Double> temperature

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



Optional<[BetaThinkingConfigParam](api/beta/messages.md)> thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



class BetaThinkingConfigEnabled:



long budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

JsonValue; type "enabled"constant"enabled"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



class BetaThinkingConfigDisabled:

JsonValue; type "disabled"constant"disabled"constant



class BetaThinkingConfigAdaptive:

JsonValue; type "adaptive"constant"adaptive"constant



Optional<Display> display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

SUMMARIZED("summarized")

OMITTED("omitted")



Optional<[BetaToolChoice](api/beta/messages.md)> toolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonValue; type "auto"constant"auto"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceAny:

The model will use any available tools.

JsonValue; type "any"constant"any"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

String name

The name of the tool to use.

JsonValue; type "tool"constant"tool"constant



Optional<Boolean> disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonValue; type "none"constant"none"constant



Optional<List<[BetaToolUnion](api/beta/messages.md)>> tools

Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](agents-and-tools/tool-use/server-tools.md), see their individual documentation as each has its own behavior (e.g., the [web search tool](agents-and-tools/tool-use/web-search-tool.md)).

Each tool definition includes:

- `name`: Name of the tool.
- `description`: Optional, but strongly-recommended description of the tool.
- `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

For example, if you defined `tools` as:

```shiki
[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
```



And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

```shiki
[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
```



You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

```shiki
[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
```



Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](agents-and-tools/tool-use/overview.md) for more details.

One of the following:



class BetaTool:



InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonValue; type "object"constant"object"constant

Optional<Properties> properties

Optional<List<String>> required



String name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



Optional<String> description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Optional<Boolean> eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Type> type



class BetaToolBash20241022:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20241022"constant"bash\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124:



JsonValue; name "bash"constant"bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "bash\_20250124"constant"bash\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250522:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250522"constant"code\_execution\_20250522"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825:



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20250825"constant"code\_execution\_20250825"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260120"constant"code\_execution\_20260120"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonValue; name "code\_execution"constant"code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "code\_execution\_20260521"constant"code\_execution\_20260521"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20241022:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20241022"constant"computer\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818:



JsonValue; name "memory"constant"memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "memory\_20250818"constant"memory\_20250818"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20250124"constant"computer\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20241022:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20241022"constant"text\_editor\_20241022"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124:

long displayHeightPx

The height of the display in pixels.

long displayWidthPx

The width of the display in pixels.



JsonValue; name "computer"constant"computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "computer\_20251124"constant"computer\_20251124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> displayNumber

The X11 display number (e.g. 0, 1) for the display.

Optional<Boolean> enableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124:



JsonValue; name "str\_replace\_editor"constant"str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250124"constant"text\_editor\_20250124"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250429"constant"text\_editor\_20250429"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728:



JsonValue; name "str\_replace\_based\_edit\_tool"constant"str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "text\_editor\_20250728"constant"text\_editor\_20250728"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<List<InputExample>> inputExamples

Optional<Long> maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20250305:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20250305"constant"web\_search\_20250305"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20250910:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20250910"constant"web\_fetch\_20250910"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20260209:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260209"constant"web\_search\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260209:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260209"constant"web\_fetch\_20260209"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260309"constant"web\_fetch\_20260309"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebSearchTool20260318:



JsonValue; name "web\_search"constant"web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_search\_20260318"constant"web\_search\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

Optional<List<String>> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



Optional<[BetaUserLocation](api/beta/messages.md)> userLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonValue; type "approximate"constant"approximate"constant

Optional<String> city

The city of the user.

Optional<String> country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

Optional<String> region

The region of the user.

Optional<String> timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260318:



JsonValue; name "web\_fetch"constant"web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "web\_fetch\_20260318"constant"web\_fetch\_20260318"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")

Optional<List<String>> allowedDomains

List of domains to allow fetching from

Optional<List<String>> blockedDomains

List of domains to block fetching from



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCitationsConfigParam](api/beta/messages.md)> citations

Citations configuration for fetched documents. Citations are disabled by default.

Optional<Boolean> enabled

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.



Optional<ResponseInclusion> responseInclusion

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

FULL("full")

EXCLUDED("excluded")

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs

Optional<Boolean> useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaAdvisorTool20260301:



Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

CLAUDE\_SONNET\_5("claude-sonnet-5")

High-performance model for coding and agents

CLAUDE\_FABLE\_5("claude-fable-5")

Next generation of intelligence for the hardest knowledge work and coding problems

CLAUDE\_MYTHOS\_5("claude-mythos-5")

Most capable model for cybersecurity and biology research

CLAUDE\_OPUS\_4\_8("claude-opus-4-8")

Frontier intelligence for long-running agents and coding

CLAUDE\_OPUS\_4\_7("claude-opus-4-7")

Frontier intelligence for long-running agents and coding

CLAUDE\_MYTHOS\_PREVIEW("claude-mythos-preview")

New class of intelligence, strongest in coding and cybersecurity

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Frontier intelligence for long-running agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks



JsonValue; name "advisor"constant"advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonValue; type "advisor\_20260301"constant"advisor\_20260301"constant



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Long> maxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

Optional<Long> maxUses

Maximum number of times the tool can be used in the API request.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolBm25\_20251119:



JsonValue; name "tool\_search\_tool\_bm25"constant"tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_BM25\_20251119("tool\_search\_tool\_bm25\_20251119")

TOOL\_SEARCH\_TOOL\_BM25("tool\_search\_tool\_bm25")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119:



JsonValue; name "tool\_search\_tool\_regex"constant"tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



Type type

One of the following:

TOOL\_SEARCH\_TOOL\_REGEX\_20251119("tool\_search\_tool\_regex\_20251119")

TOOL\_SEARCH\_TOOL\_REGEX("tool\_search\_tool\_regex")



Optional<List<AllowedCaller>> allowedCallers

One of the following:

DIRECT("direct")

CODE\_EXECUTION\_20250825("code\_execution\_20250825")

CODE\_EXECUTION\_20260120("code\_execution\_20260120")

CODE\_EXECUTION\_20260521("code\_execution\_20260521")



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")

Optional<Boolean> deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Optional<Boolean> strict

When true, guarantees schema validation on tool names and inputs



class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

String mcpServerName

Name of the MCP server to configure tools for

JsonValue; type "mcp\_toolset"constant"mcp\_toolset"constant



Optional<[BetaCacheControlEphemeral](api/beta/messages.md)> cacheControl

Create a cache control breakpoint at this content block.

JsonValue; type "ephemeral"constant"ephemeral"constant



Optional<Ttl> ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

TTL\_5M("5m")

TTL\_1H("1h")



Optional<Configs> configs

Configuration overrides for specific tools, keyed by tool name

Optional<Boolean> deferLoading

Optional<Boolean> enabled



Optional<[BetaMcpToolDefaultConfig](api/beta/messages.md)> defaultConfig

Default configuration applied to all tools from this server

Optional<Boolean> deferLoading

Optional<Boolean> enabled



DeprecatedOptional<Long> topK

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



DeprecatedOptional<Double> topP

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

##### ReturnsExpand Collapse



class BetaMessageBatch:



String id

Unique object identifier.

The format and length of IDs may change over time.

Optional<LocalDateTime> archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

Optional<LocalDateTime> cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.



Optional<LocalDateTime> endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

LocalDateTime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



ProcessingStatus processingStatus

Processing status of the Message Batch.

One of the following:

IN\_PROGRESS("in\_progress")

CANCELING("canceling")

ENDED("ended")



[BetaMessageBatchRequestCounts](api/beta/messages/batches.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



long canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



long errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



long expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

long processing

Number of requests in the Message Batch that are processing.



long succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



Optional<String> resultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



JsonValue; type "message\_batch"constant"message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Create a Message Batch

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchCreateParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatch;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .addRequest(BatchCreateParams.Request.builder()
                .customId("my-custom-id-1")
                .params(BatchCreateParams.Request.Params.builder()
                    .maxTokens(1024L)
                    .addUserMessage("Hello, world")
                    .model(Model.CLAUDE_OPUS_4_6)
                    .build())
                .build())
            .build();
        BetaMessageBatch betaMessageBatch = client.beta().messages().batches().create(params);
    }
}
```

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

---

*Copyright © Anthropic. All rights reserved.*
