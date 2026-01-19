# Delete File

Copy page

TypeScript

# Delete File

client.beta.files.delete(stringfileID, FileDeleteParams { betas } params?, RequestOptionsoptions?): [DeletedFile](api/beta.md) { id, type }

delete/v1/files/{file\_id}

Delete File

##### ParametersExpand Collapse

fileID: string

ID of the File.

params: FileDeleteParams { betas }

betas?: Array<[AnthropicBeta](api/beta.md)>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 16 more

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

DeletedFile { id, type }

id: string

ID of the deleted file.

type?: "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file\_deleted"

Delete File

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const deletedFile = await client.beta.files.delete('file_id');

console.log(deletedFile.id);
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
