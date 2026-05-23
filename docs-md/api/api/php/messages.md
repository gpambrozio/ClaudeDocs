# Messages

Copy page

PHP

# Messages

##### [Create a Message](api/messages/create.md)

$client->messages->create(int maxTokens, list<[MessageParam](api/messages.md)> messages, Model model, ?[CacheControlEphemeral](api/messages.md) cacheControl, ?string container, ?string inferenceGeo, ?[Metadata](api/messages.md) metadata, ?[OutputConfig](api/messages.md) outputConfig, ?[ServiceTier](api/messages/create.md) serviceTier, ?list<string> stopSequences, ?[System](api/messages/create.md) system, ?float temperature, ?[ThinkingConfigParam](api/messages.md) thinking, ?[ToolChoice](api/messages.md) toolChoice, ?list<[ToolUnion](api/messages.md)> tools, ?int topK, ?float topP): [Message](api/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

$client->messages->countTokens(list<[MessageParam](api/messages.md)> messages, Model model, ?[CacheControlEphemeral](api/messages.md) cacheControl, ?[OutputConfig](api/messages.md) outputConfig, ?[System](api/messages/count_tokens.md) system, ?[ThinkingConfigParam](api/messages.md) thinking, ?[ToolChoice](api/messages.md) toolChoice, ?list<[MessageCountTokensTool](api/messages.md)> tools): [MessageTokensCount](api/messages.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

[Base64ImageSource](api/messages.md)

string data

MediaType mediaType

"base64" type

[Base64PDFSource](api/messages.md)

string data

"application/pdf" mediaType

"base64" type

[BashCodeExecutionOutputBlock](api/messages.md)

string fileID

"bash\_code\_execution\_output" type

[BashCodeExecutionOutputBlockParam](api/messages.md)

string fileID

"bash\_code\_execution\_output" type

[BashCodeExecutionResultBlock](api/messages.md)

list<[BashCodeExecutionOutputBlock](api/messages.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type

[BashCodeExecutionResultBlockParam](api/messages.md)

list<[BashCodeExecutionOutputBlockParam](api/messages.md)> content

int returnCode

string stderr

string stdout

"bash\_code\_execution\_result" type

[BashCodeExecutionToolResultBlock](api/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

[BashCodeExecutionToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[BashCodeExecutionToolResultError](api/messages.md)

[BashCodeExecutionToolResultErrorCode](api/messages.md) errorCode

"bash\_code\_execution\_tool\_result\_error" type

[BashCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

[BashCodeExecutionToolResultErrorParam](api/messages.md)

[BashCodeExecutionToolResultErrorCode](api/messages.md) errorCode

"bash\_code\_execution\_tool\_result\_error" type

[CacheControlEphemeral](api/messages.md)

"ephemeral" type

?TTL ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

[CacheCreation](api/messages.md)

int ephemeral1hInputTokens

The number of input tokens used to create the 1 hour cache entry.

int ephemeral5mInputTokens

The number of input tokens used to create the 5 minute cache entry.

[CitationCharLocation](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type

[CitationCharLocationParam](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type

[CitationContentBlockLocation](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[CitationContentBlockLocationParam](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[CitationPageLocation](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type

[CitationPageLocationParam](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type

[CitationSearchResultLocationParam](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[CitationWebSearchResultLocationParam](api/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[CitationsConfig](api/messages.md)

bool enabled

[CitationsConfigParam](api/messages.md)

?bool enabled

[CitationsDelta](api/messages.md)

Citation citation

"citations\_delta" type

[CitationsSearchResultLocation](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[CitationsWebSearchResultLocation](api/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[CodeExecutionOutputBlock](api/messages.md)

string fileID

"code\_execution\_output" type

[CodeExecutionOutputBlockParam](api/messages.md)

string fileID

"code\_execution\_output" type

[CodeExecutionResultBlock](api/messages.md)

list<[CodeExecutionOutputBlock](api/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[CodeExecutionResultBlockParam](api/messages.md)

list<[CodeExecutionOutputBlockParam](api/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[CodeExecutionTool20250522](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20250825](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20260120](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionToolResultBlock](api/messages.md)

[CodeExecutionToolResultBlockContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

[CodeExecutionToolResultBlockContent](api/messages.md)

One of the following:

[CodeExecutionToolResultError](api/messages.md)

[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

"code\_execution\_tool\_result\_error" type

[CodeExecutionResultBlock](api/messages.md)

list<[CodeExecutionOutputBlock](api/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[EncryptedCodeExecutionResultBlock](api/messages.md)

list<[CodeExecutionOutputBlock](api/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[CodeExecutionToolResultBlockParam](api/messages.md)

[CodeExecutionToolResultBlockParamContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[CodeExecutionToolResultBlockParamContent](api/messages.md)

One of the following:

[CodeExecutionToolResultErrorParam](api/messages.md)

[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

"code\_execution\_tool\_result\_error" type

[CodeExecutionResultBlockParam](api/messages.md)

list<[CodeExecutionOutputBlockParam](api/messages.md)> content

int returnCode

string stderr

string stdout

"code\_execution\_result" type

[EncryptedCodeExecutionResultBlockParam](api/messages.md)

list<[CodeExecutionOutputBlockParam](api/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[CodeExecutionToolResultError](api/messages.md)

[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

"code\_execution\_tool\_result\_error" type

[CodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

[CodeExecutionToolResultErrorParam](api/messages.md)

[CodeExecutionToolResultErrorCode](api/messages.md) errorCode

"code\_execution\_tool\_result\_error" type

[Container](api/messages.md)

string id

Identifier for the container used in this request

\Datetime expiresAt

The time at which the container will expire.

[ContainerUploadBlock](api/messages.md)

string fileID

"container\_upload" type

[ContainerUploadBlockParam](api/messages.md)

string fileID

"container\_upload" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ContentBlock](api/messages.md)

One of the following:

[TextBlock](api/messages.md)

?list<[TextCitation](api/messages.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type

[ThinkingBlock](api/messages.md)

string signature

string thinking

"thinking" type

[RedactedThinkingBlock](api/messages.md)

string data

"redacted\_thinking" type

[ToolUseBlock](api/messages.md)

string id

Caller caller

Tool invocation directly from the model.

array<string,mixed> input

string name

"tool\_use" type

[ServerToolUseBlock](api/messages.md)

string id

Caller caller

Tool invocation directly from the model.

array<string,mixed> input

Name name

"server\_tool\_use" type

[WebSearchToolResultBlock](api/messages.md)

Caller caller

Tool invocation directly from the model.

[WebSearchToolResultBlockContent](api/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

[WebFetchToolResultBlock](api/messages.md)

Caller caller

Tool invocation directly from the model.

Content content

string toolUseID

"web\_fetch\_tool\_result" type

[CodeExecutionToolResultBlock](api/messages.md)

[CodeExecutionToolResultBlockContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

[BashCodeExecutionToolResultBlock](api/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

[TextEditorCodeExecutionToolResultBlock](api/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

[ToolSearchToolResultBlock](api/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

[ContainerUploadBlock](api/messages.md)

string fileID

"container\_upload" type

[ContentBlockParam](api/messages.md)

One of the following:

[TextBlockParam](api/messages.md)

string text

"text" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[TextCitationParam](api/messages.md)> citations

[ImageBlockParam](api/messages.md)

Source source

"image" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[DocumentBlockParam](api/messages.md)

Source source

"document" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

?string context

?string title

[SearchResultBlockParam](api/messages.md)

list<[TextBlockParam](api/messages.md)> content

string source

string title

"search\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

[ThinkingBlockParam](api/messages.md)

string signature

string thinking

"thinking" type

[RedactedThinkingBlockParam](api/messages.md)

string data

"redacted\_thinking" type

[ToolUseBlockParam](api/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[ToolResultBlockParam](api/messages.md)

string toolUseID

"tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[ServerToolUseBlockParam](api/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[WebSearchToolResultBlockParam](api/messages.md)

[WebSearchToolResultBlockParamContent](api/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[WebFetchToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[CodeExecutionToolResultBlockParam](api/messages.md)

[CodeExecutionToolResultBlockParamContent](api/messages.md) content

Code execution result with encrypted stdout for PFC + web\_search results.

string toolUseID

"code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[BashCodeExecutionToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"bash\_code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[TextEditorCodeExecutionToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ToolSearchToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ContainerUploadBlockParam](api/messages.md)

string fileID

"container\_upload" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ContentBlockSource](api/messages.md)

Content content

"content" type

[ContentBlockSourceContent](api/messages.md)

One of the following:

[TextBlockParam](api/messages.md)

string text

"text" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[TextCitationParam](api/messages.md)> citations

[ImageBlockParam](api/messages.md)

Source source

"image" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[DirectCaller](api/messages.md)

"direct" type

[DocumentBlock](api/messages.md)

?[CitationsConfig](api/messages.md) citations

Citation configuration for the document

Source source

?string title

The title of the document

"document" type

[DocumentBlockParam](api/messages.md)

Source source

"document" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

?string context

?string title

[EncryptedCodeExecutionResultBlock](api/messages.md)

list<[CodeExecutionOutputBlock](api/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[EncryptedCodeExecutionResultBlockParam](api/messages.md)

list<[CodeExecutionOutputBlockParam](api/messages.md)> content

string encryptedStdout

int returnCode

string stderr

"encrypted\_code\_execution\_result" type

[ImageBlockParam](api/messages.md)

Source source

"image" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[InputJSONDelta](api/messages.md)

string partialJSON

"input\_json\_delta" type

[JSONOutputFormat](api/messages.md)

array<string,mixed> schema

The JSON schema of the format

"json\_schema" type

[MemoryTool20250818](api/messages.md)

"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[Message](api/messages.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

?[Container](api/messages.md) container

Information about the container used in the request (for the code execution tool)

list<[ContentBlock](api/messages.md)> content

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

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"assistant" role

Conversational role of the generated message.

This will always be `"assistant"`.

?[RefusalStopDetails](api/messages.md) stopDetails

Structured information about a refusal.

?[StopReason](api/messages.md) stopReason

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

?string stopSequence

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

"message" type

Object type.

For Messages, this is always `"message"`.

[Usage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[MessageCountTokensTool](api/messages.md)

One of the following:

[Tool](api/messages.md)

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type

[ToolBash20250124](api/messages.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20250522](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20250825](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20260120](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[MemoryTool20250818](api/messages.md)

"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250124](api/messages.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250429](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250728](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebSearchTool20250305](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebFetchTool20250910](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebSearchTool20260209](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebFetchTool20260209](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebFetchTool20260309](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[ToolSearchToolBm25\_20251119](api/messages.md)

"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolSearchToolRegex20251119](api/messages.md)

"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[MessageDeltaUsage](api/messages.md)

?int cacheCreationInputTokens

The cumulative number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The cumulative number of input tokens read from the cache.

?int inputTokens

The cumulative number of input tokens which were used.

int outputTokens

The cumulative number of output tokens which were used.

?[ServerToolUsage](api/messages.md) serverToolUse

The number of server tool requests.

[MessageParam](api/messages.md)

Content content

Role role

[MessageTokensCount](api/messages.md)

int inputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

[Metadata](api/messages.md)

?string userID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

Model

One of the following:

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

[OutputConfig](api/messages.md)

?Effort effort

All possible effort levels.

?[JSONOutputFormat](api/messages.md) format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

[PlainTextSource](api/messages.md)

string data

"text/plain" mediaType

"text" type

[RawContentBlockDelta](api/messages.md)

One of the following:

[TextDelta](api/messages.md)

string text

"text\_delta" type

[InputJSONDelta](api/messages.md)

string partialJSON

"input\_json\_delta" type

[CitationsDelta](api/messages.md)

Citation citation

"citations\_delta" type

[ThinkingDelta](api/messages.md)

string thinking

"thinking\_delta" type

[SignatureDelta](api/messages.md)

string signature

"signature\_delta" type

[RawContentBlockDeltaEvent](api/messages.md)

[RawContentBlockDelta](api/messages.md) delta

int index

"content\_block\_delta" type

[RawContentBlockStartEvent](api/messages.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type

[RawContentBlockStopEvent](api/messages.md)

int index

"content\_block\_stop" type

[RawMessageDeltaEvent](api/messages.md)

Delta delta

"message\_delta" type

[MessageDeltaUsage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[RawMessageStartEvent](api/messages.md)

[Message](api/messages.md) message

"message\_start" type

[RawMessageStopEvent](api/messages.md)

"message\_stop" type

[RawMessageStreamEvent](api/messages.md)

One of the following:

[RawMessageStartEvent](api/messages.md)

[Message](api/messages.md) message

"message\_start" type

[RawMessageDeltaEvent](api/messages.md)

Delta delta

"message\_delta" type

[MessageDeltaUsage](api/messages.md) usage

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

[RawMessageStopEvent](api/messages.md)

"message\_stop" type

[RawContentBlockStartEvent](api/messages.md)

ContentBlock contentBlock

Response model for a file uploaded to the container.

int index

"content\_block\_start" type

[RawContentBlockDeltaEvent](api/messages.md)

[RawContentBlockDelta](api/messages.md) delta

int index

"content\_block\_delta" type

[RawContentBlockStopEvent](api/messages.md)

int index

"content\_block\_stop" type

[RedactedThinkingBlock](api/messages.md)

string data

"redacted\_thinking" type

[RedactedThinkingBlockParam](api/messages.md)

string data

"redacted\_thinking" type

[RefusalStopDetails](api/messages.md)

?Category category

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

?string explanation

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

"refusal" type

[SearchResultBlockParam](api/messages.md)

list<[TextBlockParam](api/messages.md)> content

string source

string title

"search\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

[ServerToolCaller](api/messages.md)

string toolID

"code\_execution\_20250825" type

[ServerToolCaller20260120](api/messages.md)

string toolID

"code\_execution\_20260120" type

[ServerToolUsage](api/messages.md)

int webFetchRequests

The number of web fetch tool requests.

int webSearchRequests

The number of web search tool requests.

[ServerToolUseBlock](api/messages.md)

string id

Caller caller

Tool invocation directly from the model.

array<string,mixed> input

Name name

"server\_tool\_use" type

[ServerToolUseBlockParam](api/messages.md)

string id

array<string,mixed> input

Name name

"server\_tool\_use" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[SignatureDelta](api/messages.md)

string signature

"signature\_delta" type

[StopReason](api/messages.md)

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"refusal"

[TextBlock](api/messages.md)

?list<[TextCitation](api/messages.md)> citations

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

string text

"text" type

[TextBlockParam](api/messages.md)

string text

"text" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?list<[TextCitationParam](api/messages.md)> citations

[TextCitation](api/messages.md)

One of the following:

[CitationCharLocation](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

?string fileID

int startCharIndex

"char\_location" type

[CitationPageLocation](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

?string fileID

int startPageNumber

"page\_location" type

[CitationContentBlockLocation](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

?string fileID

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[CitationsWebSearchResultLocation](api/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[CitationsSearchResultLocation](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[TextCitationParam](api/messages.md)

One of the following:

[CitationCharLocationParam](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endCharIndex

int startCharIndex

"char\_location" type

[CitationPageLocationParam](api/messages.md)

string citedText

int documentIndex

?string documentTitle

int endPageNumber

int startPageNumber

"page\_location" type

[CitationContentBlockLocationParam](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int documentIndex

?string documentTitle

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

"content\_block\_location" type

[CitationWebSearchResultLocationParam](api/messages.md)

string citedText

string encryptedIndex

?string title

"web\_search\_result\_location" type

string url

[CitationSearchResultLocationParam](api/messages.md)

string citedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

int endBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

int searchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

string source

int startBlockIndex

0-based index of the first cited block in the source's `content` array.

?string title

"search\_result\_location" type

[TextDelta](api/messages.md)

string text

"text\_delta" type

[TextEditorCodeExecutionCreateResultBlock](api/messages.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type

[TextEditorCodeExecutionCreateResultBlockParam](api/messages.md)

bool isFileUpdate

"text\_editor\_code\_execution\_create\_result" type

[TextEditorCodeExecutionStrReplaceResultBlock](api/messages.md)

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

"text\_editor\_code\_execution\_str\_replace\_result" type

[TextEditorCodeExecutionStrReplaceResultBlockParam](api/messages.md)

"text\_editor\_code\_execution\_str\_replace\_result" type

?list<string> lines

?int newLines

?int newStart

?int oldLines

?int oldStart

[TextEditorCodeExecutionToolResultBlock](api/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

[TextEditorCodeExecutionToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"text\_editor\_code\_execution\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[TextEditorCodeExecutionToolResultError](api/messages.md)

[TextEditorCodeExecutionToolResultErrorCode](api/messages.md) errorCode

?string errorMessage

"text\_editor\_code\_execution\_tool\_result\_error" type

[TextEditorCodeExecutionToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

[TextEditorCodeExecutionToolResultErrorParam](api/messages.md)

[TextEditorCodeExecutionToolResultErrorCode](api/messages.md) errorCode

"text\_editor\_code\_execution\_tool\_result\_error" type

?string errorMessage

[TextEditorCodeExecutionViewResultBlock](api/messages.md)

string content

FileType fileType

?int numLines

?int startLine

?int totalLines

"text\_editor\_code\_execution\_view\_result" type

[TextEditorCodeExecutionViewResultBlockParam](api/messages.md)

string content

FileType fileType

"text\_editor\_code\_execution\_view\_result" type

?int numLines

?int startLine

?int totalLines

[ThinkingBlock](api/messages.md)

string signature

string thinking

"thinking" type

[ThinkingBlockParam](api/messages.md)

string signature

string thinking

"thinking" type

[ThinkingConfigAdaptive](api/messages.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[ThinkingConfigDisabled](api/messages.md)

"disabled" type

[ThinkingConfigEnabled](api/messages.md)

int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[ThinkingConfigParam](api/messages.md)

One of the following:

[ThinkingConfigEnabled](api/messages.md)

int budgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

"enabled" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[ThinkingConfigDisabled](api/messages.md)

"disabled" type

[ThinkingConfigAdaptive](api/messages.md)

"adaptive" type

?Display display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

[ThinkingDelta](api/messages.md)

string thinking

"thinking\_delta" type

[Tool](api/messages.md)

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type

[ToolBash20250124](api/messages.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolChoice](api/messages.md)

One of the following:

[ToolChoiceAuto](api/messages.md)

"auto" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[ToolChoiceAny](api/messages.md)

"any" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[ToolChoiceTool](api/messages.md)

string name

The name of the tool to use.

"tool" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[ToolChoiceNone](api/messages.md)

"none" type

[ToolChoiceAny](api/messages.md)

"any" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[ToolChoiceAuto](api/messages.md)

"auto" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

[ToolChoiceNone](api/messages.md)

"none" type

[ToolChoiceTool](api/messages.md)

string name

The name of the tool to use.

"tool" type

?bool disableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

[ToolReferenceBlock](api/messages.md)

string toolName

"tool\_reference" type

[ToolReferenceBlockParam](api/messages.md)

string toolName

"tool\_reference" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ToolResultBlockParam](api/messages.md)

string toolUseID

"tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Content content

?bool isError

[ToolSearchToolBm25\_20251119](api/messages.md)

"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolSearchToolRegex20251119](api/messages.md)

"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolSearchToolResultBlock](api/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

[ToolSearchToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"tool\_search\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

[ToolSearchToolResultError](api/messages.md)

[ToolSearchToolResultErrorCode](api/messages.md) errorCode

?string errorMessage

"tool\_search\_tool\_result\_error" type

[ToolSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

[ToolSearchToolResultErrorParam](api/messages.md)

[ToolSearchToolResultErrorCode](api/messages.md) errorCode

"tool\_search\_tool\_result\_error" type

[ToolSearchToolSearchResultBlock](api/messages.md)

list<[ToolReferenceBlock](api/messages.md)> toolReferences

"tool\_search\_tool\_search\_result" type

[ToolSearchToolSearchResultBlockParam](api/messages.md)

list<[ToolReferenceBlockParam](api/messages.md)> toolReferences

"tool\_search\_tool\_search\_result" type

[ToolTextEditor20250124](api/messages.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250429](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250728](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolUnion](api/messages.md)

One of the following:

[Tool](api/messages.md)

InputSchema inputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

string name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?string description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

?bool eagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

?Type type

[ToolBash20250124](api/messages.md)

"bash" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"bash\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20250522](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250522" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20250825](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20250825" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[CodeExecutionTool20260120](api/messages.md)

"code\_execution" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"code\_execution\_20260120" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[MemoryTool20250818](api/messages.md)

"memory" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"memory\_20250818" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250124](api/messages.md)

"str\_replace\_editor" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250124" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250429](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250429" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolTextEditor20250728](api/messages.md)

"str\_replace\_based\_edit\_tool" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"text\_editor\_20250728" type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?list<array<string,mixed>> inputExamples

?int maxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebSearchTool20250305](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebFetchTool20250910](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebSearchTool20260209](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebFetchTool20260209](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebFetchTool20260309](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[ToolSearchToolBm25\_20251119](api/messages.md)

"tool\_search\_tool\_bm25" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolSearchToolRegex20251119](api/messages.md)

"tool\_search\_tool\_regex" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Type type

?list<AllowedCaller> allowedCallers

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?bool strict

When true, guarantees schema validation on tool names and inputs

[ToolUseBlock](api/messages.md)

string id

Caller caller

Tool invocation directly from the model.

array<string,mixed> input

string name

"tool\_use" type

[ToolUseBlockParam](api/messages.md)

string id

array<string,mixed> input

string name

"tool\_use" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[URLImageSource](api/messages.md)

"url" type

string url

[URLPDFSource](api/messages.md)

"url" type

string url

[Usage](api/messages.md)

?[CacheCreation](api/messages.md) cacheCreation

Breakdown of cached tokens by TTL

?int cacheCreationInputTokens

The number of input tokens used to create the cache entry.

?int cacheReadInputTokens

The number of input tokens read from the cache.

?string inferenceGeo

The geographic region where inference was performed for this request.

int inputTokens

The number of input tokens which were used.

int outputTokens

The number of output tokens which were used.

?[ServerToolUsage](api/messages.md) serverToolUse

The number of server tool requests.

?ServiceTier serviceTier

If the request used the priority, standard, or batch tier.

[UserLocation](api/messages.md)

"approximate" type

?string city

The city of the user.

?string country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

?string region

The region of the user.

?string timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

[WebFetchBlock](api/messages.md)

[DocumentBlock](api/messages.md) content

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

"web\_fetch\_result" type

string url

Fetched content URL

[WebFetchBlockParam](api/messages.md)

[DocumentBlockParam](api/messages.md) content

"web\_fetch\_result" type

string url

Fetched content URL

?string retrievedAt

ISO 8601 timestamp when the content was retrieved

[WebFetchTool20250910](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20250910" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebFetchTool20260209](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

[WebFetchTool20260309](api/messages.md)

"web\_fetch" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_fetch\_20260309" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

List of domains to allow fetching from

?list<string> blockedDomains

List of domains to block fetching from

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?[CitationsConfigParam](api/messages.md) citations

Citations configuration for fetched documents. Citations are disabled by default.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?bool useCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

[WebFetchToolResultBlock](api/messages.md)

Caller caller

Tool invocation directly from the model.

Content content

string toolUseID

"web\_fetch\_tool\_result" type

[WebFetchToolResultBlockParam](api/messages.md)

Content content

string toolUseID

"web\_fetch\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[WebFetchToolResultErrorBlock](api/messages.md)

[WebFetchToolResultErrorCode](api/messages.md) errorCode

"web\_fetch\_tool\_result\_error" type

[WebFetchToolResultErrorBlockParam](api/messages.md)

[WebFetchToolResultErrorCode](api/messages.md) errorCode

"web\_fetch\_tool\_result\_error" type

[WebFetchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

[WebSearchResultBlock](api/messages.md)

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url

[WebSearchResultBlockParam](api/messages.md)

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge

[WebSearchTool20250305](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20250305" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebSearchTool20260209](api/messages.md)

"web\_search" name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

"web\_search\_20260209" type

?list<AllowedCaller> allowedCallers

?list<string> allowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

?list<string> blockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?bool deferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

?int maxUses

Maximum number of times the tool can be used in the API request.

?bool strict

When true, guarantees schema validation on tool names and inputs

?[UserLocation](api/messages.md) userLocation

Parameters for the user's location. Used to provide more relevant search results.

[WebSearchToolRequestError](api/messages.md)

[WebSearchToolResultErrorCode](api/messages.md) errorCode

"web\_search\_tool\_result\_error" type

[WebSearchToolResultBlock](api/messages.md)

Caller caller

Tool invocation directly from the model.

[WebSearchToolResultBlockContent](api/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

[WebSearchToolResultBlockContent](api/messages.md)

One of the following:

[WebSearchToolResultError](api/messages.md)

[WebSearchToolResultErrorCode](api/messages.md) errorCode

"web\_search\_tool\_result\_error" type

list<[WebSearchResultBlock](api/messages.md)>

string encryptedContent

?string pageAge

string title

"web\_search\_result" type

string url

[WebSearchToolResultBlockParam](api/messages.md)

[WebSearchToolResultBlockParamContent](api/messages.md) content

string toolUseID

"web\_search\_tool\_result" type

?[CacheControlEphemeral](api/messages.md) cacheControl

Create a cache control breakpoint at this content block.

?Caller caller

Tool invocation directly from the model.

[WebSearchToolResultBlockParamContent](api/messages.md)

One of the following:

list<[WebSearchResultBlockParam](api/messages.md)>

string encryptedContent

string title

"web\_search\_result" type

string url

?string pageAge

[WebSearchToolRequestError](api/messages.md)

[WebSearchToolResultErrorCode](api/messages.md) errorCode

"web\_search\_tool\_result\_error" type

[WebSearchToolResultError](api/messages.md)

[WebSearchToolResultErrorCode](api/messages.md) errorCode

"web\_search\_tool\_result\_error" type

[WebSearchToolResultErrorCode](api/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

$client->messages->batches->create(list<Request> requests): [MessageBatch](api/messages.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

$client->messages->batches->retrieve(string messageBatchID): [MessageBatch](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit): Page<[MessageBatch](api/messages.md)>

GET/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

$client->messages->batches->cancel(string messageBatchID): [MessageBatch](api/messages.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

$client->messages->batches->delete(string messageBatchID): [DeletedMessageBatch](api/messages.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

$client->messages->batches->results(string messageBatchID): [MessageBatchIndividualResponse](api/messages.md)

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

[DeletedMessageBatch](api/messages.md)

string id

ID of the Message Batch.

"message\_batch\_deleted" type

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

[MessageBatch](api/messages.md)

string id

Unique object identifier.

The format and length of IDs may change over time.

?\Datetime archivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

?\Datetime cancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

?\Datetime endedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

\Datetime expiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

ProcessingStatus processingStatus

Processing status of the Message Batch.

[MessageBatchRequestCounts](api/messages.md) requestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

?string resultsURL

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

"message\_batch" type

Object type.

For Message Batches, this is always `"message_batch"`.

[MessageBatchCanceledResult](api/messages.md)

"canceled" type

[MessageBatchErroredResult](api/messages.md)

[ErrorResponse](api/$shared.md) error

"errored" type

[MessageBatchExpiredResult](api/messages.md)

"expired" type

[MessageBatchIndividualResponse](api/messages.md)

string customID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

[MessageBatchResult](api/messages.md) result

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

[MessageBatchRequestCounts](api/messages.md)

int canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

int errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

int expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

int processing

Number of requests in the Message Batch that are processing.

int succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

[MessageBatchResult](api/messages.md)

One of the following:

[MessageBatchSucceededResult](api/messages.md)

[Message](api/messages.md) message

"succeeded" type

[MessageBatchErroredResult](api/messages.md)

[ErrorResponse](api/$shared.md) error

"errored" type

[MessageBatchCanceledResult](api/messages.md)

"canceled" type

[MessageBatchExpiredResult](api/messages.md)

"expired" type

[MessageBatchSucceededResult](api/messages.md)

[Message](api/messages.md) message

"succeeded" type

---

*Copyright © Anthropic. All rights reserved.*
