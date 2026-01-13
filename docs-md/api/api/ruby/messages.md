# Messages

Copy page

Ruby

# Messages

##### [Create a Message](api/messages/create.md)

messages.create(\*\*kwargs) -> [Message](api/messages.md) { id, content, model, 5 more }

post/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

messages.count\_tokens(\*\*kwargs) -> [MessageTokensCount](api/messages.md) { input\_tokens }

post/v1/messages/count\_tokens

##### ModelsExpand Collapse

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class CacheControlEphemeral { type, ttl }

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class CacheCreation { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsConfigParam { enabled }

enabled: bool

class CitationsDelta { citation, type }

citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

ContentBlock = [TextBlock](api/messages.md) { citations, text, type }  | [ThinkingBlock](api/messages.md) { signature, thinking, type }  | [RedactedThinkingBlock](api/messages.md) { data, type }  | 3 more

Accepts one of the following:

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

ContentBlockParam = [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more }  | 7 more

Regular text content.

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class ThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

String

Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

is\_error: bool

class ServerToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class WebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class WebSearchToolRequestError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

ContentBlockSourceContent = [TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class InputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

class Message { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

MessageCountTokensTool = [Tool](api/messages.md) { input\_schema, name, cache\_control, 2 more }  | [ToolBash20250124](api/messages.md) { name, type, cache\_control }  | [ToolTextEditor20250124](api/messages.md) { name, type, cache\_control }  | 3 more

Accepts one of the following:

class Tool { input\_schema, name, cache\_control, 2 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

type: :custom

Accepts one of the following:

:custom

class ToolBash20250124 { name, type, cache\_control }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250124 { name, type, cache\_control }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250429 { name, type, cache\_control }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250728 { name, type, cache\_control, max\_characters }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

class WebSearchTool20250305 { name, type, allowed\_domains, 4 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class MessageDeltaUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class MessageParam { content, role }

content: String | Array[[ContentBlockParam](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockParam](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class ThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

String

Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

is\_error: bool

class ServerToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class WebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class WebSearchToolRequestError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

role: :user | :assistant

Accepts one of the following:

:user

:assistant

class MessageTokensCount { input\_tokens }

input\_tokens: Integer

The total number of tokens across the provided list of messages, system prompt, and tools.

class Metadata { user\_id }

user\_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

Model = :"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more | String

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

RawContentBlockDelta = [TextDelta](api/messages.md) { text, type }  | [InputJSONDelta](api/messages.md) { partial\_json, type }  | [CitationsDelta](api/messages.md) { citation, type }  | 2 more

Accepts one of the following:

class TextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class InputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

class CitationsDelta { citation, type }

citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class SignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

class RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class InputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

class CitationsDelta { citation, type }

citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class SignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

index: Integer

type: :content\_block\_delta

Accepts one of the following:

:content\_block\_delta

class RawContentBlockStartEvent { content\_block, index, type }

content\_block: [TextBlock](api/messages.md) { citations, text, type }  | [ThinkingBlock](api/messages.md) { signature, thinking, type }  | [RedactedThinkingBlock](api/messages.md) { data, type }  | 3 more

Accepts one of the following:

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

index: Integer

type: :content\_block\_start

Accepts one of the following:

:content\_block\_start

class RawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

Accepts one of the following:

:content\_block\_stop

class RawMessageDeltaEvent { delta, type, usage }

delta: { stop\_reason, stop\_sequence}

stop\_reason: [StopReason](api/messages.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

type: :message\_delta

Accepts one of the following:

:message\_delta

usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class RawMessageStartEvent { message, type }

message: [Message](api/messages.md) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message\_start

Accepts one of the following:

:message\_start

class RawMessageStopEvent { type }

type: :message\_stop

Accepts one of the following:

:message\_stop

RawMessageStreamEvent = [RawMessageStartEvent](api/messages.md) { message, type }  | [RawMessageDeltaEvent](api/messages.md) { delta, type, usage }  | [RawMessageStopEvent](api/messages.md) { type }  | 3 more

Accepts one of the following:

class RawMessageStartEvent { message, type }

message: [Message](api/messages.md) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message\_start

Accepts one of the following:

:message\_start

class RawMessageDeltaEvent { delta, type, usage }

delta: { stop\_reason, stop\_sequence}

stop\_reason: [StopReason](api/messages.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

type: :message\_delta

Accepts one of the following:

:message\_delta

usage: [MessageDeltaUsage](api/messages.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class RawMessageStopEvent { type }

type: :message\_stop

Accepts one of the following:

:message\_stop

class RawContentBlockStartEvent { content\_block, index, type }

content\_block: [TextBlock](api/messages.md) { citations, text, type }  | [ThinkingBlock](api/messages.md) { signature, thinking, type }  | [RedactedThinkingBlock](api/messages.md) { data, type }  | 3 more

Accepts one of the following:

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

index: Integer

type: :content\_block\_start

Accepts one of the following:

:content\_block\_start

class RawContentBlockDeltaEvent { delta, index, type }

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class InputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

class CitationsDelta { citation, type }

citation: [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class SignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

index: Integer

type: :content\_block\_delta

Accepts one of the following:

:content\_block\_delta

class RawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

Accepts one of the following:

:content\_block\_stop

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class RedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class ServerToolUsage { web\_search\_requests }

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class ServerToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

StopReason = :end\_turn | :max\_tokens | :stop\_sequence | 3 more

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

TextCitation = [CitationCharLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationPageLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | [CitationContentBlockLocation](api/messages.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

TextCitationParam = [CitationCharLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  | [CitationPageLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  | [CitationContentBlockLocationParam](api/messages.md) { cited\_text, document\_index, document\_title, 3 more }  | 2 more

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class TextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class ThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class ThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class ThinkingConfigEnabled { budget\_tokens, type }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

ThinkingConfigParam = [ThinkingConfigEnabled](api/messages.md) { budget\_tokens, type }  | [ThinkingConfigDisabled](api/messages.md) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class ThinkingConfigEnabled { budget\_tokens, type }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

class ThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class ThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class Tool { input\_schema, name, cache\_control, 2 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

type: :custom

Accepts one of the following:

:custom

class ToolBash20250124 { name, type, cache\_control }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

ToolChoice = [ToolChoiceAuto](api/messages.md) { type, disable\_parallel\_tool\_use }  | [ToolChoiceAny](api/messages.md) { type, disable\_parallel\_tool\_use }  | [ToolChoiceTool](api/messages.md) { name, type, disable\_parallel\_tool\_use }  | [ToolChoiceNone](api/messages.md) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

class ToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

class ToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

String

Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations }  | [ImageBlockParam](api/messages.md) { source, type, cache\_control }  | [SearchResultBlockParam](api/messages.md) { content, source, title, 3 more }  | [DocumentBlockParam](api/messages.md) { source, type, cache\_control, 3 more } ]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class SearchResultBlockParam { content, source, title, 3 more }

content: Array[[TextBlockParam](api/messages.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

class DocumentBlockParam { source, type, cache\_control, 3 more }

source: [Base64PDFSource](api/messages.md) { data, media\_type, type }  | [PlainTextSource](api/messages.md) { data, media\_type, type }  | [ContentBlockSource](api/messages.md) { content, type }  | [URLPDFSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class PlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class ContentBlockSource { content, type }

content: String | Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

String

Array[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[TextCitationParam](api/messages.md)]

Accepts one of the following:

class CitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class ImageBlockParam { source, type, cache\_control }

source: [Base64ImageSource](api/messages.md) { data, media\_type, type }  | [URLImageSource](api/messages.md) { type, url }

Accepts one of the following:

class Base64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :image

Accepts one of the following:

:image

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

Accepts one of the following:

:content

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

type: :document

Accepts one of the following:

:document

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [CitationsConfigParam](api/messages.md) { enabled }

enabled: bool

context: String

title: String

is\_error: bool

class ToolTextEditor20250124 { name, type, cache\_control }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250429 { name, type, cache\_control }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250728 { name, type, cache\_control, max\_characters }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

ToolUnion = [Tool](api/messages.md) { input\_schema, name, cache\_control, 2 more }  | [ToolBash20250124](api/messages.md) { name, type, cache\_control }  | [ToolTextEditor20250124](api/messages.md) { name, type, cache\_control }  | 3 more

Accepts one of the following:

class Tool { input\_schema, name, cache\_control, 2 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

type: :custom

Accepts one of the following:

:custom

class ToolBash20250124 { name, type, cache\_control }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250124 { name, type, cache\_control }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250429 { name, type, cache\_control }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class ToolTextEditor20250728 { name, type, cache\_control, max\_characters }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

class WebSearchTool20250305 { name, type, allowed\_domains, 4 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ToolUseBlockParam { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class URLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class URLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class Usage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

class WebSearchResultBlock { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

class WebSearchResultBlockParam { encrypted\_content, title, type, 2 more }

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class WebSearchTool20250305 { name, type, allowed\_domains, 4 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class WebSearchToolRequestError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

WebSearchToolResultBlockContent = [WebSearchToolResultError](api/messages.md) { error\_code, type }  | Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

class WebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class WebSearchToolRequestError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [CacheControlEphemeral](api/messages.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

WebSearchToolResultBlockParamContent = Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ] | [WebSearchToolRequestError](api/messages.md) { error\_code, type }

Accepts one of the following:

Array[[WebSearchResultBlockParam](api/messages.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class WebSearchToolRequestError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

messages.batches.create(\*\*kwargs) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages.batches.retrieve(message\_batch\_id) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages.batches.list(\*\*kwargs) -> Page<[MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

get/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages.batches.cancel(message\_batch\_id) -> [MessageBatch](api/messages.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages.batches.delete(message\_batch\_id) -> [DeletedMessageBatch](api/messages.md) { id, type }

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages.batches.results(message\_batch\_id) -> [MessageBatchIndividualResponse](api/messages.md) { custom\_id, result }

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class DeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

:message\_batch\_deleted

class MessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel\_initiated\_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended\_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing\_status: :in\_progress | :canceling | :ended

Processing status of the Message Batch.

Accepts one of the following:

:in\_progress

:canceling

:ended

request\_counts: [MessageBatchRequestCounts](api/messages.md) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: :message\_batch

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

:message\_batch

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](api/$shared.md) { error, request\_id, type }

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class AuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class PermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class NotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class RateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class APIErrorObject { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class OverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchIndividualResponse { custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult { message, type }

message: [Message](api/messages.md) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](api/$shared.md) { error, request\_id, type }

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class AuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class PermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class NotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class RateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class APIErrorObject { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class OverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

MessageBatchResult = [MessageBatchSucceededResult](api/messages.md) { message, type }  | [MessageBatchErroredResult](api/messages.md) { error, type }  | [MessageBatchCanceledResult](api/messages.md) { type }  | [MessageBatchExpiredResult](api/messages.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult { message, type }

message: [Message](api/messages.md) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](api/$shared.md) { error, request\_id, type }

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class AuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class PermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class NotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class RateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class APIErrorObject { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class OverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchSucceededResult { message, type }

message: [Message](api/messages.md) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array[[ContentBlock](api/messages.md)]

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

class TextBlock { citations, text, type }

citations: Array[[TextCitation](api/messages.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class CitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class CitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class CitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class CitationsSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash[Symbol, untyped]

name: :web\_search

Accepts one of the following:

:web\_search

type: :server\_tool\_use

Accepts one of the following:

:server\_tool\_use

class WebSearchToolResultBlock { content, tool\_use\_id, type }

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[WebSearchResultBlock](api/messages.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop\_reason: [StopReason](api/messages.md)

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

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](api/messages.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [CacheCreation](api/messages.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [ServerToolUsage](api/messages.md) { web\_search\_requests }

The number of server tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded