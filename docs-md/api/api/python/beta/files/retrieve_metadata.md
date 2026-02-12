# Get File Metadata

Copy page

Python

# Get File Metadata

beta.files.retrieve\_metadata(strfile\_id, FileRetrieveMetadataParams\*\*kwargs)  -> [FileMetadata](api/beta.md)

GET/v1/files/{file\_id}

Get File Metadata

##### ParametersExpand Collapse

file\_id: str

ID of the File.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 17 more]

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

##### ReturnsExpand Collapse

class FileMetadata: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

created\_at: datetime

RFC 3339 datetime string representing when the file was created.

filename: str

Original filename of the uploaded file.

mime\_type: str

MIME type of the file.

size\_bytes: int

Size of the file in bytes.

type: Literal["file"]

Object type.

For files, this is always `"file"`.

downloadable: Optional[bool]

Whether the file can be downloaded.

Get File Metadata

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
file_metadata = client.beta.files.retrieve_metadata(
    file_id="file_id",
)
print(file_metadata.id)
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
