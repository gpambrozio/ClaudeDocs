# Count tokens in a Message

Copy page

SDK language

C#

# Count tokens in a Message

[BetaMessageTokensCount](api/beta.md) Beta.Messages.CountTokens(MessageCountTokensParamsparameters, CancellationTokencancellationToken = default)

POST/v1/messages/count\_tokens

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

##### ParametersExpand Collapse



MessageCountTokensParams parameters



required IReadOnlyList<[BetaMessageParam](api/beta.md)> messages

Body param: Input messages.

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

IReadOnlyList<[BetaContentBlockParam](api/beta.md)>

One of the following:



class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

class BetaImageBlockParam:



required Source Source

One of the following:



class BetaBase64ImageSource:

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

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url



class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestDocumentBlock:



required Source Source

One of the following:



class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class BetaContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

One of the following:



class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

class BetaImageBlockParam:



required Source Source

One of the following:



class BetaBase64ImageSource:

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

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url



class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url



class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title



class BetaSearchResultBlockParam:



required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled



class BetaThinkingBlockParam:

required string Signature

required string Thinking

JsonElement Type "thinking"constant



class BetaRedactedThinkingBlockParam:

required string Data

JsonElement Type "redacted\_thinking"constant



class BetaToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

JsonElement Type "tool\_use"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class BetaToolResultBlockParam:

required string ToolUseID

JsonElement Type "tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

class BetaImageBlockParam:



required Source Source

One of the following:



class BetaBase64ImageSource:

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

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url



class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaSearchResultBlockParam:



required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md) Citations

Boolean Enabled



class BetaRequestDocumentBlock:



required Source Source

One of the following:



class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class BetaContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

One of the following:



class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

class BetaImageBlockParam:



required Source Source

One of the following:



class BetaBase64ImageSource:

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

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url



class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url



class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

Boolean Enabled

string? Context

string? Title



class BetaToolReferenceBlockParam:

Tool reference block that can be included in tool\_result content.

required string ToolName

JsonElement Type "tool\_reference"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaServerToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input



required Name Name

One of the following:

"advisor"Advisor

"web\_search"WebSearch

"web\_fetch"WebFetch

"code\_execution"CodeExecution

"bash\_code\_execution"BashCodeExecution

"text\_editor\_code\_execution"TextEditorCodeExecution

"tool\_search\_tool\_regex"ToolSearchToolRegex

"tool\_search\_tool\_bm25"ToolSearchToolBm25

JsonElement Type "server\_tool\_use"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class BetaWebSearchToolResultBlockParam:



required [BetaWebSearchToolResultBlockParamContent](api/beta.md) Content

One of the following:



IReadOnlyList<[BetaWebSearchResultBlockParam](api/beta.md)>

required string EncryptedContent

required string Title

JsonElement Type "web\_search\_result"constant

required string Url

string? PageAge



class BetaWebSearchToolRequestError:



required [BetaWebSearchToolResultErrorCode](api/beta.md) ErrorCode

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class BetaWebFetchToolResultBlockParam:



required Content Content

One of the following:



class BetaWebFetchToolResultErrorBlockParam:



required [BetaWebFetchToolResultErrorCode](api/beta.md) ErrorCode

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

class BetaWebFetchBlockParam:



required [BetaRequestDocumentBlock](api/beta.md) Content



required Source Source

One of the following:



class BetaBase64PdfSource:

required string Data

JsonElement MediaType "application/pdf"constant

JsonElement Type "base64"constant



class BetaPlainTextSource:

required string Data

JsonElement MediaType "text/plain"constant

JsonElement Type "text"constant



class BetaContentBlockSource:



required Content Content

One of the following:

string



IReadOnlyList<[BetaContentBlockSourceContent](api/beta.md)>

One of the following:



class BetaTextBlockParam:

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

class BetaImageBlockParam:



required Source Source

One of the following:



class BetaBase64ImageSource:

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

class BetaUrlImageSource:

JsonElement Type "url"constant

required string Url



class BetaFileImageSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "image"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaUrlPdfSource:

JsonElement Type "url"constant

required string Url



class BetaFileDocumentSource:

required string FileID

JsonElement Type "file"constant

JsonElement Type "document"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaDirectCaller:

Tool invocation directly from the model.

JsonElement Type "direct"constant



class BetaServerToolCaller:

Tool invocation generated by a server-side tool.

required string ToolID

JsonElement Type "code\_execution\_20250825"constant



class BetaServerToolCaller20260120:

required string ToolID

JsonElement Type "code\_execution\_20260120"constant



class BetaAdvisorToolResultBlockParam:



required Content Content

One of the following:



class BetaAdvisorToolResultErrorParam:



required ErrorCode ErrorCode

One of the following:

"max\_uses\_exceeded"MaxUsesExceeded

"prompt\_too\_long"PromptTooLong

"too\_many\_requests"TooManyRequests

"overloaded"Overloaded

"unavailable"Unavailable

"execution\_time\_exceeded"ExecutionTimeExceeded

"model\_not\_found"ModelNotFound

JsonElement Type "advisor\_tool\_result\_error"constant



class BetaAdvisorResultBlockParam:

required string Text

JsonElement Type "advisor\_result"constant

string? StopReason



class BetaAdvisorRedactedResultBlockParam:

required string EncryptedContent

Opaque blob produced by a prior response; must be round-tripped verbatim.

JsonElement Type "advisor\_redacted\_result"constant

string? StopReason

required string ToolUseID

JsonElement Type "advisor\_tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCodeExecutionToolResultBlockParam:



required [BetaCodeExecutionToolResultBlockParamContent](api/beta.md) Content

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam:



required [BetaCodeExecutionToolResultErrorCode](api/beta.md) ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "code\_execution\_tool\_result\_error"constant



class BetaCodeExecutionResultBlockParam:



required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "code\_execution\_result"constant



class BetaEncryptedCodeExecutionResultBlockParam:

Code execution result with encrypted stdout for PFC + web\_search results.



required IReadOnlyList<[BetaCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "code\_execution\_output"constant

required string EncryptedStdout

required Long ReturnCode

required string Stderr

JsonElement Type "encrypted\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "code\_execution\_tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaBashCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam:



required ErrorCode ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"output\_file\_too\_large"OutputFileTooLarge

JsonElement Type "bash\_code\_execution\_tool\_result\_error"constant



class BetaBashCodeExecutionResultBlockParam:



required IReadOnlyList<[BetaBashCodeExecutionOutputBlockParam](api/beta.md)> Content

required string FileID

JsonElement Type "bash\_code\_execution\_output"constant

required Long ReturnCode

required string Stderr

required string Stdout

JsonElement Type "bash\_code\_execution\_result"constant

required string ToolUseID

JsonElement Type "bash\_code\_execution\_tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaTextEditorCodeExecutionToolResultBlockParam:



required Content Content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam:



required ErrorCode ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

"file\_not\_found"FileNotFound

JsonElement Type "text\_editor\_code\_execution\_tool\_result\_error"constant

string? ErrorMessage



class BetaTextEditorCodeExecutionViewResultBlockParam:

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

class BetaTextEditorCodeExecutionCreateResultBlockParam:

required Boolean IsFileUpdate

JsonElement Type "text\_editor\_code\_execution\_create\_result"constant



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:

JsonElement Type "text\_editor\_code\_execution\_str\_replace\_result"constant

IReadOnlyList<string>? Lines

Long? NewLines

Long? NewStart

Long? OldLines

Long? OldStart

required string ToolUseID

JsonElement Type "text\_editor\_code\_execution\_tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolSearchToolResultBlockParam:



required Content Content

One of the following:



class BetaToolSearchToolResultErrorParam:



required ErrorCode ErrorCode

One of the following:

"invalid\_tool\_input"InvalidToolInput

"unavailable"Unavailable

"too\_many\_requests"TooManyRequests

"execution\_time\_exceeded"ExecutionTimeExceeded

JsonElement Type "tool\_search\_tool\_result\_error"constant

string? ErrorMessage



class BetaToolSearchToolSearchResultBlockParam:



required IReadOnlyList<[BetaToolReferenceBlockParam](api/beta.md)> ToolReferences

required string ToolName

JsonElement Type "tool\_reference"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMcpToolUseBlockParam:

required string ID

required IReadOnlyDictionary<string, JsonElement> Input

required string Name

required string ServerName

The name of the MCP server

JsonElement Type "mcp\_tool\_use"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaRequestMcpToolResultBlockParam:

required string ToolUseID

JsonElement Type "mcp\_tool\_result"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

Boolean IsError



class BetaContainerUploadBlockParam:

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

required string FileID

JsonElement Type "container\_upload"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCompactionBlockParam:

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

JsonElement Type "compaction"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

string? Content

Summary of previously compacted content, or null if compaction failed

string? EncryptedContent

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam:

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



required IReadOnlyList<[BetaTextBlockParam](api/beta.md)> Content

System instruction text blocks.

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaFallbackBlockParam:

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and never rendered into the prompt,
not validated against the request's `fallbacks` chain or top-level
`model`, and stripped before the sticky-routing cache key is computed.

Callers should echo the assistant turn verbatim — block included. The
block's position is load-bearing for thinking verification: the thinking
runs on either side of a fallback hop carry independently-rooted
verification hash chains, and this block is the only record of where one
chain ends and the next begins. When thinking runs flank the boundary,
omitting the block merges the runs into one contiguous span whose hashes
cannot verify (the request is rejected), and moving it into the middle of
a single run splits that run's chain and is likewise rejected; between
non-thinking blocks the block's placement has no verification effect.



required [BetaFallbackInfoParam](api/beta.md) From

Identifies one hop of a fallback transition.

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

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model



required [BetaFallbackInfoParam](api/beta.md) To

Identifies one hop of a fallback transition.

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

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model

JsonElement Type "fallback"constant



required Role Role

One of the following:

"user"User

"assistant"Assistant

"system"System



required [Model](api/messages.md) model

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

[BetaCacheControlEphemeral](api/beta.md)? cacheControl

Body param: Top-level cache control automatically applies a cache\_control marker to the last cacheable block in the request.



[BetaContextManagementConfig](api/beta.md)? contextManagement

Body param: Context management configuration.

This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.



IReadOnlyList<[BetaRequestMcpServerUrlDefinition](api/beta.md)> mcpServers

Body param: MCP servers to be utilized in this request

required string Name

JsonElement Type "url"constant

required string Url

string? AuthorizationToken



[BetaRequestMcpServerToolConfiguration](api/beta.md)? ToolConfiguration

IReadOnlyList<string>? AllowedTools

Boolean? Enabled

[BetaOutputConfig](api/beta.md) outputConfig

Body param: Configuration options for the model's output, such as the output format.



Deprecated[BetaJsonOutputFormat](api/beta.md)? outputFormat

Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](build-with-claude/structured-outputs.md)

A schema to specify Claude's output format in responses. This parameter will be removed in a future release.



[Speed](api/beta/messages/count_tokens.md)? speed

Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

"standard"Standard

"fast"Fast



[System](api/beta/messages/count_tokens.md) system

Body param: System prompt.

A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

string



IReadOnlyList<[BetaTextBlockParam](api/beta.md)>

required string Text

JsonElement Type "text"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyList<[BetaTextCitationParam](api/beta.md)>? Citations

One of the following:



class BetaCitationCharLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndCharIndex

required Long StartCharIndex

JsonElement Type "char\_location"constant



class BetaCitationPageLocationParam:

required string CitedText

required Long DocumentIndex

required string? DocumentTitle

required Long EndPageNumber

required Long StartPageNumber

JsonElement Type "page\_location"constant



class BetaCitationContentBlockLocationParam:

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

class BetaCitationWebSearchResultLocationParam:

required string CitedText

required string EncryptedIndex

required string? Title

JsonElement Type "web\_search\_result\_location"constant

required string Url



class BetaCitationSearchResultLocationParam:

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

[BetaThinkingConfigParam](api/beta.md) thinking

Body param: Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

[BetaToolChoice](api/beta.md) toolChoice

Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.



IReadOnlyList<Tool> tools

Body param: Definitions of tools that the model may use.

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



class BetaTool:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolBash20241022:



JsonElement Name "bash"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "bash\_20241022"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolBash20250124:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCodeExecutionTool20250522:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCodeExecutionTool20250825:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaCodeExecutionTool20260120:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolComputerUse20241022:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.



JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20241022"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolComputerUse20250124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.



JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20250124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20241022:



JsonElement Name "str\_replace\_editor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "text\_editor\_20241022"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolComputerUse20251124:

required Long DisplayHeightPx

The height of the display in pixels.

required Long DisplayWidthPx

The width of the display in pixels.



JsonElement Name "computer"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "computer\_20251124"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

Long? DisplayNumber

The X11 display number (e.g. 0, 1) for the display.

Boolean EnableZoom

Whether to enable an action to take a zoomed-in screenshot of the screen.

IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolTextEditor20250429:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolTextEditor20250728:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaWebSearchTool20250305:

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

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebFetchTool20250910:

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

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

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

class BetaWebSearchTool20260209:

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

IReadOnlyList<string>? AllowedDomains

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

IReadOnlyList<string>? BlockedDomains

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaUserLocation](api/beta.md)? UserLocation

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

class BetaWebFetchTool20260209:

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

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

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

class BetaWebFetchTool20260309:

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

IReadOnlyList<string>? AllowedDomains

List of domains to allow fetching from

IReadOnlyList<string>? BlockedDomains

List of domains to block fetching from



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCitationsConfigParam](api/beta.md)? Citations

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

class BetaAdvisorTool20260301:

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

"claude-opus-4-0"ClaudeOpus4\_0

Powerful model for complex tasks

"claude-opus-4-20250514"ClaudeOpus4\_20250514

Powerful model for complex tasks

"claude-sonnet-4-0"ClaudeSonnet4\_0

High-performance model with extended thinking

"claude-sonnet-4-20250514"ClaudeSonnet4\_20250514

High-performance model with extended thinking

"claude-3-haiku-20240307"Claude\_3\_Haiku\_20240307

Fast and cost-effective model



JsonElement Name "advisor"constant

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

JsonElement Type "advisor\_20260301"constant



IReadOnlyList<AllowedCaller> AllowedCallers

One of the following:

"direct"Direct

"code\_execution\_20250825"CodeExecution20250825

"code\_execution\_20260120"CodeExecution20260120



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

[BetaCacheControlEphemeral](api/beta.md)? Caching

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

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

Long? MaxTokens

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

Long? MaxUses

Maximum number of times the tool can be used in the API request.

Boolean Strict

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolBm25\_20251119:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaToolSearchToolRegex20251119:

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



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

class BetaMcpToolset:

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

required string McpServerName

Name of the MCP server to configure tools for

JsonElement Type "mcp\_toolset"constant



[BetaCacheControlEphemeral](api/beta.md)? CacheControl

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

IReadOnlyDictionary<string, [BetaMcpToolConfig](api/beta.md)>? Configs

Configuration overrides for specific tools, keyed by tool name

Boolean DeferLoading

Boolean Enabled



[BetaMcpToolDefaultConfig](api/beta.md) DefaultConfig

Default configuration applied to all tools from this server

Boolean DeferLoading

Boolean Enabled



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

##### ReturnsExpand Collapse



class BetaMessageTokensCount:



required [BetaCountTokensContextManagementResponse](api/beta.md)? ContextManagement

Information about context management applied to the message.

required Long OriginalInputTokens

The original token count before context management was applied

required Long InputTokens

The total number of tokens across the provided list of messages, system prompt, and tools.

Count tokens in a Message

C#

```shiki
MessageCountTokensParams parameters = new()
{
    Messages =
    [
        new()
        {
            Content = "Hello, world",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus4_6,
};

var betaMessageTokensCount = await client.Beta.Messages.CountTokens(parameters);

Console.WriteLine(betaMessageTokensCount);
```

Response 200



```shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

##### Returns Examples

Response 200



```shiki
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

---

*Copyright © Anthropic. All rights reserved.*
