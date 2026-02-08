# Delete File

Copy page

Ruby

# Delete File

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta.md) { id, type }

delete/v1/files/{file\_id}

Delete File

##### ParametersExpand Collapse

file\_id: String

ID of the File.

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

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file\_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

:file\_deleted

Delete File

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

deleted_file = anthropic.beta.files.delete("file_id")

puts(deleted_file)
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
