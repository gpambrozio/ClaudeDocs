# Create a Message Batch

Copy page



C#

# Create a Message Batch

[MessageBatch](api/messages.md) Messages.Batches.Create(BatchCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/batches

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse



BatchCreateParams parameters



required IReadOnlyList<Request> requests

List of requests for prompt completion. Each is an individual request to create a Message.



required string CustomID

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

maxLength64

minLength1



required Params Params

Messages API creation parameters for the individual request.

See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.



required Long MaxTokens

The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

Set to `0` to populate the [prompt cache](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

Different models have different maximum values for this parameter. See [models](https://docs.claude.com/en/docs/models-overview) for details.

minimum0



required IReadOnlyList<[MessageParam](api/messages.md)> Messages

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

See [input examples](https://docs.claude.com/en/api/messages-examples).

Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

There is a limit of 100,000 messages in a single request.



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockParam](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class ThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class RedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant



class ToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class ToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Content Content

One of the following:

string



IReadOnlyList<Block>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class SearchResultBlockParam:



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

required string Source

required string Title

JsonElement Type "search\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md) Citations

Boolean Enabled



class DocumentBlockParam:



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title



class ToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean IsError



class ServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebSearchToolResultBlockParam:



required [WebSearchToolResultBlockParamContent](api/messages.md) Content

One of the following:



IReadOnlyList<[WebSearchResultBlockParam](api/messages.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class WebSearchToolRequestError:



required [WebSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"max\_uses\_exceeded"MaxUsesExceeded

"too\_many\_requests"TooManyRequests

"query\_too\_long"QueryTooLong

"request\_too\_large"RequestTooLarge

JsonElement Type "web\_search\_tool\_result\_error"constant

required string ToolUseID

JsonElement Type "web\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class WebFetchToolResultBlockParam:



required Content Content

One of the following:



class WebFetchToolResultErrorBlockParam:



required [WebFetchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"url\_too\_long"UrlTooLong

"url\_not\_allowed"UrlNotAllowed

"url\_not\_in\_prior\_context"UrlNotInPriorContext

"url\_not\_accessible"UrlNotAccessible

"unsupported\_content\_type"UnsupportedContentType

"too\_many\_requests"TooManyRequests

"max\_uses\_exceeded"MaxUsesExceeded

"unavailable"Unavailable

JsonElement Type "web\_fetch\_tool\_result\_error"constant



class WebFetchBlockParam:



required [DocumentBlockParam](api/messages.md) Content



required Source Source

One of the following:



class Base64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class PlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class ContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[ContentBlockSourceContent](api/messages.md)>

One of the following:



class TextBlockParam:

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



class ImageBlockParam:



required Source Source

One of the following:



class Base64ImageSource:

required string Data



required MediaType MediaType

One of the following:

"image/jpeg"ImageJpeg

"image/png"ImagePng

"image/gif"ImageGif

"image/webp"ImageWebP

JsonElement Type "base64"constant



class UrlImageSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "image"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "content"constant



class UrlPdfSource:

JsonElement Type "url"constant

required string Url

JsonElement Type "document"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Boolean Enabled

string? Context

string? Title

JsonElement Type "web\_fetch\_result"constant

required string Url

Fetched content URL

string? RetrievedAt

ISO 8601 timestamp when the content was retrieved

required string ToolUseID

JsonElement Type "web\_fetch\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



Caller Caller

Tool invocation directly from the model.

One of the following:



class DirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class ServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class ServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class CodeExecutionToolResultBlockParam:



required [CodeExecutionToolResultBlockParamContent](api/messages.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class CodeExecutionToolResultErrorParam:



required [CodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class CodeExecutionResultBlockParam:



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class EncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[CodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class BashCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BashCodeExecutionToolResultErrorParam:



required [BashCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BashCodeExecutionResultBlockParam:



required IReadOnlyList<[BashCodeExecutionOutputBlockParam](api/messages.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class TextEditorCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class TextEditorCodeExecutionToolResultErrorParam:



required [TextEditorCodeExecutionToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class TextEditorCodeExecutionViewResultBlockParam:

required string Content



required FileType FileType

One of the following:

"text"Text

"image"Image

"pdf"Pdf

JsonElement Type "text\_editor\_code\_execution\_view\_result"constant

Long? NumLines

Long? StartLine

Long? TotalLines



class TextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class TextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ToolSearchToolResultBlockParam:



required Content Content

One of the following:



class ToolSearchToolResultErrorParam:



required [ToolSearchToolResultErrorCode](api/messages.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class ToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[ToolReferenceBlockParam](api/messages.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

JsonElement Type "tool\_search\_tool\_search\_result"constant

required string ToolUseID

JsonElement Type "tool\_search\_tool\_result"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class ContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



class MidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



required IReadOnlyList<[TextBlockParam](api/messages.md)> Content

System instruction text blocks.

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant

JsonElement Type "mid\_conv\_system"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



required Role Role

One of the following:

"user"User

"assistant"Assistant

"system"System



required [Model](api/messages.md) Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

"claude-fable-5"ClaudeFable5

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"ClaudeMythos5

Most capable model for cybersecurity and biology research

"claude-opus-4-8"ClaudeOpus4\_8

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"ClaudeMythosPreview

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"ClaudeOpus4\_6

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

"claude-opus-4-1"ClaudeOpus4\_1

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"ClaudeOpus4\_1\_20250805

Exceptional model for specialized complex tasks



[CacheControlEphemeral](api/messages.md)? CacheControl

Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

string? Container

Container identifier for reuse across requests.

string? InferenceGeo

Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.



[Metadata](api/messages.md) Metadata

An object describing metadata about the request.



string? UserID

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



[OutputConfig](api/messages.md) OutputConfig

Configuration options for the model's output, such as the output format.



Effort? Effort

All possible effort levels.

One of the following:

"low"Low

"medium"Medium

"high"High

"xhigh"Xhigh

"max"Max



[JsonOutputFormat](api/messages.md)? Format

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

required IReadOnlyDictionary<string, JsonElement> Schema

The JSON schema of the format

JsonElement Type "json\_schema"constant



ServiceTier ServiceTier

Determines whether to use priority capacity (if available) or standard capacity for this request.

Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

One of the following:

"auto"Auto

"standard\_only"StandardOnly



IReadOnlyList<string> StopSequences

Custom text sequences that will cause the model to stop generating.

Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.



Boolean Stream

Whether to incrementally stream the response using server-sent events.

See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.



System System

System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

One of the following:

string



IReadOnlyList<[TextBlockParam](api/messages.md)>

required string Text

JsonElement Type "text"constant



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



IReadOnlyList<[TextCitationParam](api/messages.md)>? Citations

One of the following:



class CitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class CitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class CitationContentBlockLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

required Long DocumentIndex

required string? DocumentTitle



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

JsonElement Type "content\_block\_location"constant



class CitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class CitationSearchResultLocationParam:



required string CitedText

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



required Long EndBlockIndex

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



required Long SearchResultIndex

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

required string Source

required Long StartBlockIndex

0-based index of the first cited block in the source's `content` array.

required string? Title

JsonElement Type "search\_result\_location"constant



DeprecatedDouble Temperature

Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



[ThinkingConfigParam](api/messages.md) Thinking

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:



class ThinkingConfigEnabled:



required Long BudgetTokens

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

JsonElement Type "enabled"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



class ThinkingConfigDisabled:

JsonElement Type "disabled"constant



class ThinkingConfigAdaptive:

JsonElement Type "adaptive"constant



Display? Display

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"Summarized

"omitted"Omitted



[ToolChoice](api/messages.md) ToolChoice

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



class ToolChoiceAuto:

The model will automatically decide whether to use tools.

JsonElement Type "auto"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class ToolChoiceAny:

The model will use any available tools.

JsonElement Type "any"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceTool:

The model will use the specified tool with `tool_choice.name`.

required string Name

The name of the tool to use.

JsonElement Type "tool"constant



Boolean DisableParallelToolUse

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class ToolChoiceNone:

The model will not be allowed to use tools.

JsonElement Type "none"constant



IReadOnlyList<[ToolUnion](api/messages.md)> Tools

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

See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

One of the following:



class Tool:



required InputSchema InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

JsonElement Type "object"constant

IReadOnlyDictionary<string, JsonElement>? Properties

IReadOnlyList<string>? Required



required string Name

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



string Description

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

Boolean? EagerInputStreaming

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Type? Type



class ToolBash20250124:



JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250522:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250522"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20250825:



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20250825"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260120:

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260120"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class CodeExecutionTool20260521:

Code execution tool with REPL state persistence.



JsonElement Name "code\_execution"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "code\_execution\_20260521"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class MemoryTool20250818:



JsonElement Name "memory"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "memory\_20250818"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250124:



JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250429:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250429"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolTextEditor20250728:



JsonElement Name "str\_replace\_based\_edit\_tool"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20250728"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Long? MaxCharacters

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20250305:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20250305"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20250910:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20250910"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebSearchTool20260209:



JsonElement Name "web\_search"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_search\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



[UserLocation](api/messages.md)? UserLocation

Parameters for the user's location. Used to provide more relevant search results.

JsonElement Type "approximate"constant

string? City

The city of the user.

string? Country

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

string? Region

The region of the user.

string? Timezone

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class WebFetchTool20260209:



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260209"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class WebFetchTool20260309:

Web fetch tool with use\_cache parameter for bypassing cached content.



JsonElement Name "web\_fetch"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "web\_fetch\_20260309"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h



[CitationsConfigParam](api/messages.md)? Citations

Citations configuration for fetched documents. Citations are disabled by default.

Boolean Enabled

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Long? MaxContentTokens

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs

Boolean UseCache

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class ToolSearchToolBm25\_20251119:



JsonElement Name "tool\_search\_tool\_bm25"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_bm25\_20251119"ToolSearchToolBm25\_20251119

"tool\_search\_tool\_bm25"ToolSearchToolBm25



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class ToolSearchToolRegex20251119:



JsonElement Name "tool\_search\_tool\_regex"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



required Type Type

One of the following:

"tool\_search\_tool\_regex\_20251119"ToolSearchToolRegex20251119

"tool\_search\_tool\_regex"ToolSearchToolRegex



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120

"code\_execution\_20260521"CodeExecution20260521



[CacheControlEphemeral](api/messages.md)? CacheControl

Create a cache control breakpoint at this content block.

JsonElement Type "ephemeral"constant



Ttl Ttl

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

"5m"Ttl5m

"1h"Ttl1h

Boolean DeferLoading

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



DeprecatedLong TopK

Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



DeprecatedDouble TopP

Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0

##### ReturnsExpand Collapse



class MessageBatch:



required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset? ArchivedAt

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

required DateTimeOffset? CancelInitiatedAt

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the Message Batch was created.



required DateTimeOffset? EndedAt

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

required DateTimeOffset ExpiresAt

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



required ProcessingStatus ProcessingStatus

Processing status of the Message Batch.

One of the following:

"in\_progress"InProgress

"canceling"Canceling

"ended"Ended



required [MessageBatchRequestCounts](api/messages.md) RequestCounts

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



required Long Canceled

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



required Long Errored

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



required Long Expired

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

required Long Processing

Number of requests in the Message Batch that are processing.



required Long Succeeded

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



required string? ResultsUrl

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



JsonElement Type "message\_batch"constant

Object type.

For Message Batches, this is always `"message_batch"`.

Create a Message Batch

C#

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
                CacheControl = new() { Ttl = Ttl.Ttl5m },
                Container = "container",
                InferenceGeo = "inference_geo",
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
                ServiceTier = ServiceTier.Auto,
                StopSequences =
                [
                    "string"
                ],
                Stream = true,
                System = new(

                    [
                        new TextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new CitationCharLocationParam()
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
                Thinking = new ThinkingConfigAdaptive()
                {
                    Display = Display.Summarized
                },
                ToolChoice = new ToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new Tool()
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

var messageBatch = await client.Messages.Batches.Create(parameters);

Console.WriteLine(messageBatch);
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
