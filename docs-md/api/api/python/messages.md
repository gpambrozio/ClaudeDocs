# Messages

Copy page

Python

# Messages

##### [Create a Message](api/messages/create.md)

messages.create(MessageCreateParams\*\*kwargs)  -> [Message](api/messages.md)

post/v1/messages

##### [Count tokens in a Message](api/messages/count_tokens.md)

messages.count\_tokens(MessageCountTokensParams\*\*kwargs)  -> [MessageTokensCount](api/messages.md)

post/v1/messages/count\_tokens

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

Accepts one of the following:

"base64"

class Base64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class CacheControlEphemeral: …

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

Accepts one of the following:

"char\_location"

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

Accepts one of the following:

"char\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

type: Literal["citations\_delta"]

Accepts one of the following:

"citations\_delta"

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

ContentBlock = [ContentBlock](api/messages.md)

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

ContentBlockParam = Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 7 more]

Regular text content.

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

is\_error: Optional[bool]

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

WebSearchToolResultBlockItem = List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

ContentBlockSourceContent = [ContentBlockSourceContent](api/messages.md)

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"input\_json\_delta"

class JSONOutputFormat: …

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]

Accepts one of the following:

"json\_schema"

class Message: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

MessageCountTokensTool = [MessageCountTokensTool](api/messages.md)

Accepts one of the following:

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

Accepts one of the following:

"object"

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal["bash\_20250124"]

Accepts one of the following:

"bash\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_editor"

type: Literal["text\_editor\_20250124"]

Accepts one of the following:

"text\_editor\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250429"]

Accepts one of the following:

"text\_editor\_20250429"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250728"]

Accepts one of the following:

"text\_editor\_20250728"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web\_search"

type: Literal["web\_search\_20250305"]

Accepts one of the following:

"web\_search\_20250305"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

Accepts one of the following:

"approximate"

city: Optional[str]

The city of the user.

maxLength255

minLength1

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional[str]

The region of the user.

maxLength255

minLength1

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class MessageDeltaUsage: …

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

minimum0

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

class MessageParam: …

content: Union[str, List[Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 8 more]]]

Accepts one of the following:

ContentUnionMember0 = str

ContentUnionMember1 = List[Union[[TextBlockParam](api/messages.md), [ImageBlockParam](api/messages.md), [DocumentBlockParam](api/messages.md), 8 more]]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

is\_error: Optional[bool]

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

WebSearchToolResultBlockItem = List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

maxLength256

Model = Union[Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more], str]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

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

Accepts one of the following:

"json\_schema"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

RawContentBlockDelta = [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

Accepts one of the following:

"text\_delta"

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

Accepts one of the following:

"input\_json\_delta"

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

type: Literal["citations\_delta"]

Accepts one of the following:

"citations\_delta"

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

Accepts one of the following:

"thinking\_delta"

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

Accepts one of the following:

"signature\_delta"

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

Accepts one of the following:

"text\_delta"

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

Accepts one of the following:

"input\_json\_delta"

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

type: Literal["citations\_delta"]

Accepts one of the following:

"citations\_delta"

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

Accepts one of the following:

"thinking\_delta"

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

Accepts one of the following:

"signature\_delta"

index: int

type: Literal["content\_block\_delta"]

Accepts one of the following:

"content\_block\_delta"

class RawContentBlockStartEvent: …

content\_block: ContentBlock

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

index: int

type: Literal["content\_block\_start"]

Accepts one of the following:

"content\_block\_start"

class RawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]

Accepts one of the following:

"content\_block\_stop"

class RawMessageDeltaEvent: …

delta: Delta

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

Accepts one of the following:

"message\_delta"

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

minimum0

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

class RawMessageStartEvent: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["message\_start"]

Accepts one of the following:

"message\_start"

class RawMessageStopEvent: …

type: Literal["message\_stop"]

Accepts one of the following:

"message\_stop"

RawMessageStreamEvent = [RawMessageStreamEvent](api/messages.md)

Accepts one of the following:

class RawMessageStartEvent: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["message\_start"]

Accepts one of the following:

"message\_start"

class RawMessageDeltaEvent: …

delta: Delta

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

Accepts one of the following:

"message\_delta"

usage: [MessageDeltaUsage](api/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.

minimum0

output\_tokens: int

The cumulative number of output tokens which were used.

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

class RawMessageStopEvent: …

type: Literal["message\_stop"]

Accepts one of the following:

"message\_stop"

class RawContentBlockStartEvent: …

content\_block: ContentBlock

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

index: int

type: Literal["content\_block\_start"]

Accepts one of the following:

"content\_block\_start"

class RawContentBlockDeltaEvent: …

delta: [RawContentBlockDelta](api/messages.md)

Accepts one of the following:

class TextDelta: …

text: str

type: Literal["text\_delta"]

Accepts one of the following:

"text\_delta"

class InputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]

Accepts one of the following:

"input\_json\_delta"

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

type: Literal["citations\_delta"]

Accepts one of the following:

"citations\_delta"

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

Accepts one of the following:

"thinking\_delta"

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

Accepts one of the following:

"signature\_delta"

index: int

type: Literal["content\_block\_delta"]

Accepts one of the following:

"content\_block\_delta"

class RawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]

Accepts one of the following:

"content\_block\_stop"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class RedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class SearchResultBlockParam: …

content: List[[TextBlockParam](api/messages.md)]

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

class ServerToolUsage: …

web\_search\_requests: int

The number of web search tool requests.

minimum0

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class ServerToolUseBlockParam: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class SignatureDelta: …

signature: str

type: Literal["signature\_delta"]

Accepts one of the following:

"signature\_delta"

StopReason = Literal["end\_turn", "max\_tokens", "stop\_sequence", 3 more]

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

TextCitation = [TextCitation](api/messages.md)

Accepts one of the following:

class CitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

TextCitationParam = [TextCitationParam](api/messages.md)

Accepts one of the following:

class CitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

class TextDelta: …

text: str

type: Literal["text\_delta"]

Accepts one of the following:

"text\_delta"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class ThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class ThinkingConfigAdaptive: …

type: Literal["adaptive"]

Accepts one of the following:

"adaptive"

class ThinkingConfigDisabled: …

type: Literal["disabled"]

Accepts one of the following:

"disabled"

class ThinkingConfigEnabled: …

budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal["enabled"]

Accepts one of the following:

"enabled"

ThinkingConfigParam = [ThinkingConfigParam](api/messages.md)

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

Accepts one of the following:

"enabled"

class ThinkingConfigDisabled: …

type: Literal["disabled"]

Accepts one of the following:

"disabled"

class ThinkingConfigAdaptive: …

type: Literal["adaptive"]

Accepts one of the following:

"adaptive"

class ThinkingDelta: …

thinking: str

type: Literal["thinking\_delta"]

Accepts one of the following:

"thinking\_delta"

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

Accepts one of the following:

"object"

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal["bash\_20250124"]

Accepts one of the following:

"bash\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

ToolChoice = [ToolChoice](api/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]

Accepts one of the following:

"auto"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]

Accepts one of the following:

"any"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]

Accepts one of the following:

"tool"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]

Accepts one of the following:

"none"

class ToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]

Accepts one of the following:

"any"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]

Accepts one of the following:

"auto"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class ToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]

Accepts one of the following:

"none"

class ToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]

Accepts one of the following:

"tool"

disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class ToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]

Accepts one of the following:

"tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

ContentUnionMember0 = str

Content = List[Content]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

source: str

title: str

type: Literal["search\_result"]

Accepts one of the following:

"search\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"application/pdf"

type: Literal["base64"]

Accepts one of the following:

"base64"

class PlainTextSource: …

data: str

media\_type: Literal["text/plain"]

Accepts one of the following:

"text/plain"

type: Literal["text"]

Accepts one of the following:

"text"

class ContentBlockSource: …

content: Union[str, List[[ContentBlockSourceContent](api/messages.md)]]

Accepts one of the following:

ContentUnionMember0 = str

ContentContentBlockSourceContent = List[[ContentBlockSourceContent](api/messages.md)]

Accepts one of the following:

class TextBlockParam: …

text: str

type: Literal["text"]

Accepts one of the following:

"text"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"char\_location"

class CitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationSearchResultLocationParam: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

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

Accepts one of the following:

"base64"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["image"]

Accepts one of the following:

"image"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

Accepts one of the following:

"content"

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

type: Literal["document"]

Accepts one of the following:

"document"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

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

is\_error: Optional[bool]

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_editor"

type: Literal["text\_editor\_20250124"]

Accepts one of the following:

"text\_editor\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250429"]

Accepts one of the following:

"text\_editor\_20250429"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250728"]

Accepts one of the following:

"text\_editor\_20250728"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

ToolUnion = [ToolUnion](api/messages.md)

Accepts one of the following:

class Tool: …

input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

Accepts one of the following:

"object"

properties: Optional[Dict[str, object]]

required: Optional[List[str]]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]

Accepts one of the following:

"custom"

class ToolBash20250124: …

name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal["bash\_20250124"]

Accepts one of the following:

"bash\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250124: …

name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_editor"

type: Literal["text\_editor\_20250124"]

Accepts one of the following:

"text\_editor\_20250124"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250429: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250429"]

Accepts one of the following:

"text\_editor\_20250429"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class ToolTextEditor20250728: …

name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str\_replace\_based\_edit\_tool"

type: Literal["text\_editor\_20250728"]

Accepts one of the following:

"text\_editor\_20250728"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web\_search"

type: Literal["web\_search\_20250305"]

Accepts one of the following:

"web\_search\_20250305"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

Accepts one of the following:

"approximate"

city: Optional[str]

The city of the user.

maxLength255

minLength1

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional[str]

The region of the user.

maxLength255

minLength1

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class URLImageSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

class URLPDFSource: …

type: Literal["url"]

Accepts one of the following:

"url"

url: str

class Usage: …

cache\_creation: Optional[CacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

class WebSearchResultBlock: …

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

class WebSearchResultBlockParam: …

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

page\_age: Optional[str]

class WebSearchTool20250305: …

name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web\_search"

type: Literal["web\_search\_20250305"]

Accepts one of the following:

"web\_search\_20250305"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

user\_location: Optional[UserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

Accepts one of the following:

"approximate"

city: Optional[str]

The city of the user.

maxLength255

minLength1

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional[str]

The region of the user.

maxLength255

minLength1

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class WebSearchToolRequestError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

WebSearchToolResultBlockContent = [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

class WebSearchToolResultBlockParam: …

content: [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

WebSearchToolResultBlockItem = List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

cache\_control: Optional[CacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]

Accepts one of the following:

"ephemeral"

ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

WebSearchToolResultBlockParamContent = [WebSearchToolResultBlockParamContent](api/messages.md)

Accepts one of the following:

WebSearchToolResultBlockItem = List[[WebSearchResultBlockParam](api/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

page\_age: Optional[str]

class WebSearchToolRequestError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

#### MessagesBatches

##### [Create a Message Batch](api/messages/batches/create.md)

messages.batches.create(BatchCreateParams\*\*kwargs)  -> [MessageBatch](api/messages.md)

post/v1/messages/batches

##### [Retrieve a Message Batch](api/messages/batches/retrieve.md)

messages.batches.retrieve(strmessage\_batch\_id)  -> [MessageBatch](api/messages.md)

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/messages/batches/list.md)

messages.batches.list(BatchListParams\*\*kwargs)  -> SyncPage[[MessageBatch](api/messages.md)]

get/v1/messages/batches

##### [Cancel a Message Batch](api/messages/batches/cancel.md)

messages.batches.cancel(strmessage\_batch\_id)  -> [MessageBatch](api/messages.md)

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/messages/batches/delete.md)

messages.batches.delete(strmessage\_batch\_id)  -> [DeletedMessageBatch](api/messages.md)

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/messages/batches/results.md)

messages.batches.results(strmessage\_batch\_id)  -> [MessageBatchIndividualResponse](api/messages.md)

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class DeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal["message\_batch\_deleted"]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message\_batch\_deleted"

class MessageBatch: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel\_initiated\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended\_at: Optional[datetime]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

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

Accepts one of the following:

"message\_batch"

class MessageBatchCanceledResult: …

type: Literal["canceled"]

Accepts one of the following:

"canceled"

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

Accepts one of the following:

"invalid\_request\_error"

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

Accepts one of the following:

"authentication\_error"

class BillingError: …

message: str

type: Literal["billing\_error"]

Accepts one of the following:

"billing\_error"

class PermissionError: …

message: str

type: Literal["permission\_error"]

Accepts one of the following:

"permission\_error"

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

Accepts one of the following:

"not\_found\_error"

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

Accepts one of the following:

"rate\_limit\_error"

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

Accepts one of the following:

"timeout\_error"

class APIErrorObject: …

message: str

type: Literal["api\_error"]

Accepts one of the following:

"api\_error"

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

Accepts one of the following:

"overloaded\_error"

request\_id: Optional[str]

type: Literal["error"]

Accepts one of the following:

"error"

type: Literal["errored"]

Accepts one of the following:

"errored"

class MessageBatchExpiredResult: …

type: Literal["expired"]

Accepts one of the following:

"expired"

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

Accepts one of the following:

"succeeded"

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

Accepts one of the following:

"invalid\_request\_error"

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

Accepts one of the following:

"authentication\_error"

class BillingError: …

message: str

type: Literal["billing\_error"]

Accepts one of the following:

"billing\_error"

class PermissionError: …

message: str

type: Literal["permission\_error"]

Accepts one of the following:

"permission\_error"

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

Accepts one of the following:

"not\_found\_error"

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

Accepts one of the following:

"rate\_limit\_error"

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

Accepts one of the following:

"timeout\_error"

class APIErrorObject: …

message: str

type: Literal["api\_error"]

Accepts one of the following:

"api\_error"

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

Accepts one of the following:

"overloaded\_error"

request\_id: Optional[str]

type: Literal["error"]

Accepts one of the following:

"error"

type: Literal["errored"]

Accepts one of the following:

"errored"

class MessageBatchCanceledResult: …

type: Literal["canceled"]

Accepts one of the following:

"canceled"

class MessageBatchExpiredResult: …

type: Literal["expired"]

Accepts one of the following:

"expired"

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

MessageBatchResult = [MessageBatchResult](api/messages.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

Accepts one of the following:

"succeeded"

class MessageBatchErroredResult: …

error: [ErrorResponse](api/$shared.md)

error: [ErrorObject](api/$shared.md)

Accepts one of the following:

class InvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

Accepts one of the following:

"invalid\_request\_error"

class AuthenticationError: …

message: str

type: Literal["authentication\_error"]

Accepts one of the following:

"authentication\_error"

class BillingError: …

message: str

type: Literal["billing\_error"]

Accepts one of the following:

"billing\_error"

class PermissionError: …

message: str

type: Literal["permission\_error"]

Accepts one of the following:

"permission\_error"

class NotFoundError: …

message: str

type: Literal["not\_found\_error"]

Accepts one of the following:

"not\_found\_error"

class RateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

Accepts one of the following:

"rate\_limit\_error"

class GatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

Accepts one of the following:

"timeout\_error"

class APIErrorObject: …

message: str

type: Literal["api\_error"]

Accepts one of the following:

"api\_error"

class OverloadedError: …

message: str

type: Literal["overloaded\_error"]

Accepts one of the following:

"overloaded\_error"

request\_id: Optional[str]

type: Literal["error"]

Accepts one of the following:

"error"

type: Literal["errored"]

Accepts one of the following:

"errored"

class MessageBatchCanceledResult: …

type: Literal["canceled"]

Accepts one of the following:

"canceled"

class MessageBatchExpiredResult: …

type: Literal["expired"]

Accepts one of the following:

"expired"

class MessageBatchSucceededResult: …

message: [Message](api/messages.md)

id: str

Unique object identifier.

The format and length of IDs may change over time.

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

Accepts one of the following:

"char\_location"

class CitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]

Accepts one of the following:

"page\_location"

class CitationContentBlockLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_block\_index: int

file\_id: Optional[str]

start\_block\_index: int

type: Literal["content\_block\_location"]

Accepts one of the following:

"content\_block\_location"

class CitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

Accepts one of the following:

"web\_search\_result\_location"

url: str

class CitationsSearchResultLocation: …

cited\_text: str

end\_block\_index: int

search\_result\_index: int

source: str

start\_block\_index: int

title: Optional[str]

type: Literal["search\_result\_location"]

Accepts one of the following:

"search\_result\_location"

text: str

type: Literal["text"]

Accepts one of the following:

"text"

class ThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]

Accepts one of the following:

"thinking"

class RedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]

Accepts one of the following:

"redacted\_thinking"

class ToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]

Accepts one of the following:

"tool\_use"

class ServerToolUseBlock: …

id: str

input: Dict[str, object]

name: Literal["web\_search"]

Accepts one of the following:

"web\_search"

type: Literal["server\_tool\_use"]

Accepts one of the following:

"server\_tool\_use"

class WebSearchToolResultBlock: …

content: [WebSearchToolResultBlockContent](api/messages.md)

Accepts one of the following:

class WebSearchToolResultError: …

error\_code: Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

Accepts one of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

Accepts one of the following:

"web\_search\_tool\_result\_error"

UnionMember1 = List[[WebSearchResultBlock](api/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

Accepts one of the following:

"web\_search\_result"

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]

Accepts one of the following:

"web\_search\_tool\_result"

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

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

Accepts one of the following:

"message"

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

minimum0

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

minimum0

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.

minimum0

output\_tokens: int

The number of output tokens which were used.

minimum0

server\_tool\_use: Optional[ServerToolUsage]

The number of server tool requests.

web\_search\_requests: int

The number of web search tool requests.

minimum0

service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal["succeeded"]

Accepts one of the following:

"succeeded"

---

*Copyright © Anthropic. All rights reserved.*
