# Get File Metadata

Copy page

Ruby

# Get File Metadata

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

get/v1/files/{file\_id}

Get File Metadata

##### ParametersExpand Collapse

file\_id: String

ID of the File.

anthropic\_beta: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 16 more

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

##### ReturnsExpand Collapse

class FileMetadata { id, created\_at, filename, 4 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: String

Original filename of the uploaded file.

maxLength500

minLength1

mime\_type: String

MIME type of the file.

maxLength255

minLength1

size\_bytes: Integer

Size of the file in bytes.

minimum0

type: :file

Object type.

For files, this is always `"file"`.

Accepts one of the following:

:file

downloadable: bool

Whether the file can be downloaded.

Get File Metadata

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(file_metadata)
```

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "x",
  "mime_type": "x",
  "size_bytes": 0,
  "type": "file",
  "downloadable": true
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "x",
  "mime_type": "x",
  "size_bytes": 0,
  "type": "file",
  "downloadable": true
}
```