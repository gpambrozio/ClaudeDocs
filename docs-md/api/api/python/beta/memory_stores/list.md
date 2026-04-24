# ListMemoryStores

Copy page

Python

# ListMemoryStores

beta.memory\_stores.list(MemoryStoreListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryStore](api/beta.md)]

GET/v1/memory\_stores

ListMemoryStores

##### ParametersExpand Collapse

created\_at\_gte: Optional[Union[str, datetime]]

Return stores created at or after this time (inclusive).

created\_at\_lte: Optional[Union[str, datetime]]

Return stores created at or before this time (inclusive).

include\_archived: Optional[[bool](api/beta/memory_stores/list.md)]

Query parameter for include\_archived

limit: Optional[int]

Query parameter for limit

page: Optional[str]

Query parameter for page

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]

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

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsMemoryStore: …

id: str

type: Literal["memory\_store"]

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: Optional[datetime]

A timestamp in RFC 3339 format

description: Optional[str]

metadata: Optional[Dict[str, str]]

name: Optional[str]

updated\_at: Optional[datetime]

A timestamp in RFC 3339 format

ListMemoryStores

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.memory_stores.list()
page = page.data[0]
print(page.id)
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
