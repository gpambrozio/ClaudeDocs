# Add Session Resource

Copy page

Python

# Add Session Resource

beta.sessions.resources.add(strsession\_id, ResourceAddParams\*\*kwargs)  -> [BetaManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

Add Session Resource

##### ParametersExpand Collapse

session\_id: str

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

mount\_path: Optional[str]

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 20 more]

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

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsFileResource: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

file\_id: str

mount\_path: str

type: Literal["file"]

updated\_at: datetime

A timestamp in RFC 3339 format

Add Session Resource

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_file_resource = client.beta.sessions.resources.add(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    file_id="file_011CNha8iCJcU1wXNR6q4V8w",
    type="file",
)
print(beta_managed_agents_file_resource.id)
```

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
