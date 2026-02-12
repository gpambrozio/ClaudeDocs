# List Files

Copy page

Ruby

# List Files

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 4 more } >

GET/v1/files

List Files

##### ParametersExpand Collapse

after\_id: String

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before\_id: String

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

limit: Integer

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

anthropic\_beta: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 17 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

##### ReturnsExpand Collapse

class FileMetadata { id, created\_at, filename, 4 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

filename: String

Original filename of the uploaded file.

mime\_type: String

MIME type of the file.

size\_bytes: Integer

Size of the file in bytes.

type: :file

Object type.

For files, this is always `"file"`.

downloadable: bool

Whether the file can be downloaded.

List Files

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.files.list

puts(page)
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
