# Create a Message Batch

Copy page

C#

# Create a Message Batch

[BetaMessageBatch](api/beta.md) Beta.Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse

BatchCreateParams parameters

required IReadOnlyList<Request> requests

Body param: List of requests for prompt completion. Each is an individual request to create a Message.

required string CustomID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1

required Params Params

Messages API creation parameters for the individual request.

See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

required Long MaxTokens

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum1

required IReadOnlyList<[BetaMessageParam](api/beta.md)> Messages

Input messages.

Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

Example with a single `user` message:

```shiki
[{"role": "user", "content": "Hello, Claude"}]
```

Example with multiple conversational turns:

```shiki
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

Example with a partially-filled response from Claude:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("},
]
```

Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

```shiki
{"role": "user", "content": "Hello, Claude"}
```

```shiki
{"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
```

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockParam](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant

class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant

class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<Block>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaSearchResultBlockParam:

required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled

class BetaRequestDocumentBlock:

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required Name Name

Accepts one of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Caller Caller

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant

class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant

class BetaWebSearchToolResultBlockParam:

required [BetaWebSearchToolResultBlockParamContent](api/beta.md) Content

Accepts one of the following:

IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge

class BetaWebSearchToolRequestError:

required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaWebFetchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam:

required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant

class BetaWebFetchBlockParam:

required [BetaRequestDocumentBlock](api/beta.md) Content

required Source Source

Accepts one of the following:

class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant

class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant

class BetaContentBlockSource:

required Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

Accepts one of the following:

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

class BetaImageBlockParam:

required Source Source

Accepts one of the following:

class BetaBase64ImageSource:

required string Data

required MediaType MediaType

Accepts one of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url

class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url

class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCodeExecutionToolResultBlockParam:

required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam:

required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant

class BetaCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaBashCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant

class BetaBashCodeExecutionResultBlockParam:

required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaTextEditorCodeExecutionToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage

class BetaTextEditorCodeExecutionViewResultBlockParam:

required string Content

required FileType FileType

Accepts one of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaToolSearchToolResultBlockParam:

required Content Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam:

required ErrorCode ErrorCode

Accepts one of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

class BetaToolSearchToolSearchResultBlockParam:

required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Content Content

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Boolean IsError

class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

required string? Content

Summary of previously compacted content, or null if compaction failed

JsonElement Type "compaction"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

required Role Role

Accepts one of the following:

"user"User

"assistant"Assistant

required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"Claude3\_7SonnetLatest

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"Claude3\_7Sonnet20250219

High-performance model with early extended thinking

"claude-3-5-haiku-latest"Claude3\_5HaikuLatest

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"Claude3\_5Haiku20241022

Our fastest model

"claude-haiku-4-5"ClaudeHaiku4\_5

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-4-sonnet-20250514"Claude4Sonnet20250514

High-performance model with extended thinking

"claude-sonnet-4-5"ClaudeSonnet4\_5

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

Our best model for real-world agents and coding

"claude-opus-4-0"ClaudeOpus4\_0

Our most capable model

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Our most capable model

"claude-4-opus-20250514"Claude4Opus20250514

Our most capable model

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Our most capable model

"claude-3-opus-latest"Claude3OpusLatest

Excels at writing and complex tasks

"claude-3-opus-20240229"Claude\_3\_Opus\_20240229

Excels at writing and complex tasks

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Our previous most fast and cost-effective

Container? Container

Container identifier for reuse across requests.

Accepts one of the following:

class BetaContainerParams:

Container parameters with skills to be loaded.

string? ID

Container id

IReadOnlyList<[BetaSkillParams](api/beta.md)>? Skills

List of skills to load in the container

required string SkillID

Skill ID

required Type Type

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"Anthropic

"custom"Custom

string Version

Skill version or 'latest' for most recent version

string

[BetaContextManagementConfig](api/beta.md)? ContextManagement

Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

IReadOnlyList<Edit> Edits

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit:

JsonElement Type "clear\_tool\_uses\_20250919"constant

[BetaInputTokensClearAtLeast](api/beta.md)? ClearAtLeast

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

JsonElement Type "input\_tokens"constant

required Long Value

ClearToolInputs? ClearToolInputs

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

Boolean

IReadOnlyList<string>

IReadOnlyList<string>? ExcludeTools

Tool names whose uses are preserved from clearing

[BetaToolUsesKeep](api/beta.md) Keep

Number of tool uses to retain in the conversation

JsonElement Type "tool\_uses"constant

required Long Value

Trigger Trigger

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger:

JsonElement Type "input\_tokens"constant

required Long Value

class BetaToolUsesTrigger:

JsonElement Type "tool\_uses"constant

required Long Value

class BetaClearThinking20251015Edit:

JsonElement Type "clear\_thinking\_20251015"constant

Keep Keep

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns:

JsonElement Type "thinking\_turns"constant

required Long Value

class BetaAllThinkingTurns:

JsonElement Type "all"constant

class UnionMember2:

class BetaCompact20260112Edit:

Automatically compact older context when reaching the configured trigger threshold.

JsonElement Type "compact\_20260112"constant

string? Instructions

Additional instructions for summarization.

Boolean PauseAfterCompaction

Whether to pause after compaction and return the compaction block to the user.

[BetaInputTokensTrigger](api/beta.md)? Trigger

When to trigger compaction. Defaults to 150000 input tokens.

JsonElement Type "input\_tokens"constant

required Long Value

string? InferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

IReadOnlyList<[BetaRequestMcpServerUrlDefinition](api/beta.md)> McpServers

MCP servers to be utilized in this request

required string Name

JsonElement Type "url"constant

required string Url

string? AuthorizationToken

[BetaRequestMcpServerToolConfiguration](api/beta.md)? ToolConfiguration

IReadOnlyList<string>? AllowedTools

Boolean? Enabled

[BetaMetadata](api/beta.md) Metadata

An object describing metadata about the request.

string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

[BetaOutputConfig](api/beta.md) OutputConfig

Configuration options for the model's output, such as the output format.

Effort? Effort

All possible effort levels.

Accepts one of the following:

"low"Low

"medium"Medium

"high"High

"max"Max

[BetaJsonOutputFormat](api/beta.md)? Format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

Deprecated[BetaJsonOutputFormat](api/beta.md)? OutputFormat

Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant

ServiceTier ServiceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

Accepts one of the following:

"auto"Auto

"standard\_only"StandardOnly

Speed? Speed

The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

Accepts one of the following:

"standard"Standard

"fast"Fast

IReadOnlyList<string> StopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

Boolean Stream

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

System System

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

Accepts one of the following:

string

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

Accepts one of the following:

class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant

class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant

class BetaCitationContentBlockLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndBlockIndex

required Long StartBlockIndex

JsonElement Type "content\_block\_location"constant

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url

class BetaCitationSearchResultLocationParam:

required string CitedText

required Long EndBlockIndex

required Long SearchResultIndex

required string Source

required Long StartBlockIndex

required string? Title

JsonElement Type "search\_result\_location"constant

Double Temperature

Amount of randomness injected into the response.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0

[BetaThinkingConfigParam](api/beta.md) Thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled:

required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant

class BetaThinkingConfigDisabled:

JsonElement Type "disabled"constant

class BetaThinkingConfigAdaptive:

JsonElement Type "adaptive"constant

[BetaToolChoice](api/beta.md) ToolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant

Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant

IReadOnlyList<[BetaToolUnion](api/beta.md)> Tools

Definitions of tools that the model may use.

If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

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

Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

Accepts one of the following:

class BetaTool:

required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required

required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type

class BetaToolBash20241022:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124:

JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825:

JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818:

JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20241022"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.

JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20251124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124:

JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728:

JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305:

JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

UserLocation? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20250910:

JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

[BetaCitationsConfigParam](api/beta.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25\_20251119:

JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119:

JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

required Type Type

Accepts one of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex

IReadOnlyList<AllowedCaller> AllowedCallers

Accepts one of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp\_toolset"constant

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant

Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"Ttl5m

"1h"Ttl1h

IReadOnlyDictionary<string, [BetaMcpToolConfig](api/beta.md)>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled

[BetaMcpToolDefaultConfig](api/beta.md) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled

Long TopK

Only sample from the top K options for each subsequent token.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only. You usually only need to use `temperature`.

minimum0

Double TopP

Use nucleus sampling.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

Recommended for advanced use cases only. You usually only need to use `temperature`.

maximum1

minimum0

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

##### ReturnsExpand Collapse

class BetaMessageBatch:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset? ArchivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

required DateTimeOffset? CancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the Message Batch was created.

required DateTimeOffset? EndedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

required DateTimeOffset ExpiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

required ProcessingStatus ProcessingStatus

Processing status of the Message Batch.

Accepts one of the following:

"in\_progress"InProgress

"canceling"Canceling

"ended"Ended

required [BetaMessageBatchRequestCounts](api/beta.md) RequestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.

required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

required string? ResultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

JsonElement Type "message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Create a Message Batch

C#

```shiki
BatchCreateParams parameters = new()
{
    Requests =
    [
        new()
        {
            CustomID = "my-custom-id-1",
            Params = new()
            {
                MaxTokens = 1024,
                Messages =
                [
                    new()
                    {
                        Content = "Hello, world",
                        Role = Role.User,
                    },
                ],
                Model = Model.ClaudeOpus4_6,
                Container = new BetaContainerParams()
                {
                    ID = "id",
                    Skills =
                    [
                        new()
                        {
                            SkillID = "x",
                            Type = Type.Anthropic,
                            Version = "x",
                        },
                    ],
                },
                ContextManagement = new()
                {
                    Edits =
                    [
                        new BetaClearToolUses20250919Edit()
                        {
                            ClearAtLeast = new(0),
                            ClearToolInputs = true,
                            ExcludeTools =
                            [
                                "string"
                            ],
                            Keep = new(0),
                            Trigger = new BetaInputTokensTrigger(1),
                        },
                    ],
                },
                InferenceGeo = "inference_geo",
                McpServers =
                [
                    new()
                    {
                        Name = "name",
                        Url = "url",
                        AuthorizationToken = "authorization_token",
                        ToolConfiguration = new()
                        {
                            AllowedTools =
                            [
                                "string"
                            ],
                            Enabled = true,
                        },
                    },
                ],
                Metadata = new()
                {
                    UserID = "13803d75-b4b5-4c3e-b2a2-6f21399b021b"
                },
                OutputConfig = new()
                {
                    Effort = Effort.Low,
                    Format = new()
                    {
                        Schema = new Dictionary<string, JsonElement>()
                        {
                            { "foo", JsonSerializer.SerializeToElement("bar") }
                        },
                    },
                },
                OutputFormat = new()
                {
                    Schema = new Dictionary<string, JsonElement>()
                    {
                        { "foo", JsonSerializer.SerializeToElement("bar") }
                    },
                },
                ServiceTier = ServiceTier.Auto,
                Speed = Speed.Standard,
                StopSequences =
                [
                    "string"
                ],
                Stream = true,
                System = new(

                    [
                        new BetaTextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new BetaCitationCharLocationParam()
                                {
                                    CitedText = "cited_text",
                                    DocumentIndex = 0,
                                    DocumentTitle = "x",
                                    EndCharIndex = 0,
                                    StartCharIndex = 0,
                                },
                            ],
                        },
                    ]
                ),
                Temperature = 1,
                Thinking = new BetaThinkingConfigEnabled(1024),
                ToolChoice = new BetaToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new BetaTool()
                    {
                        InputSchema = new()
                        {
                            Properties = new Dictionary<string, JsonElement>()
                            {
                                { "location", JsonSerializer.SerializeToElement("bar") },
                                { "unit", JsonSerializer.SerializeToElement("bar") },
                            },
                            Required =
                            [
                                "location"
                            ],
                        },
                        Name = "name",
                        AllowedCallers =
                        [
                            AllowedCaller.Direct
                        ],
                        CacheControl = new() { Ttl = Ttl.Ttl5m },
                        DeferLoading = true,
                        Description = "Get the current weather in a given location",
                        EagerInputStreaming = true,
                        InputExamples =
                        [
                            new Dictionary<string, JsonElement>()
                            {
                                { "foo", JsonSerializer.SerializeToElement("bar") },
                            },
                        ],
                        Strict = true,
                        Type = Type.Custom,
                    },
                ],
                TopK = 5,
                TopP = 0.7,
            },
        },
    ],
};

var betaMessageBatch = await client.Beta.Messages.Batches.Create(parameters);

Console.WriteLine(betaMessageBatch);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
