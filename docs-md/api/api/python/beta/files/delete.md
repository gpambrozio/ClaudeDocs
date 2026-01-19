# Delete File

Copy page

Python

# Delete File

beta.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [DeletedFile](api/beta.md)

delete/v1/files/{file\_id}

Delete File

##### ParametersExpand Collapse

file\_id: str

ID of the File.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = str

UnionMember1 = Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 16 more]

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

##### ReturnsExpand Collapse

class DeletedFile: …

id: str

ID of the deleted file.

type: Optional[Literal["file\_deleted"]]

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file\_deleted"

Delete File

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
deleted_file = client.beta.files.delete(
    file_id="file_id",
)
print(deleted_file.id)
```

Response 200

```shiki
{
  "id": "id",
  "type": "file_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "type": "file_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
