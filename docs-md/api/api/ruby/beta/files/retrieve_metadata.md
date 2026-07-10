# Get File Metadata

Copy page



Ruby

# Get File Metadata

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta/files.md) { id, created\_at, filename, 5 more }

GET/v1/files/{file\_id}

Get File Metadata

##### ParametersExpand Collapse

file\_id: String

ID of the File.



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

:"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class FileMetadata { id, created\_at, filename, 5 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

filename: String

Original filename of the uploaded file.

mime\_type: String

MIME type of the file.

size\_bytes: Integer

Size of the file in bytes.



type: :file

Object type.

For files, this is always `"file"`.

downloadable: bool

Whether the file can be downloaded.



scope: [BetaFileScope](api/beta/files.md) { id, type } 

The scope of this file, indicating the context in which it was created (e.g., a session).

id: String

The ID of the scoping resource (e.g., the session ID).

type: :session

The type of scope (e.g., `"session"`).

Get File Metadata

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(file_metadata)
```

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
