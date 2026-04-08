# List User Profiles

Copy page

Python

# List User Profiles

beta.user\_profiles.list(UserProfileListParams\*\*kwargs)  -> SyncPageCursorV2[[BetaUserProfile](api/beta.md)]

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

limit: Optional[int]

Query parameter for limit

order: Optional[Literal["asc", "desc"]]

Query parameter for order

Accepts one of the following:

"asc"

"desc"

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

"user-profiles-2026-03-24"

##### ReturnsExpand Collapse

class BetaUserProfile: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

metadata: Dict[str, str]

trust\_grants: Dict[str, [BetaUserProfileTrustGrant](api/beta.md)]

status: str

type: str

updated\_at: datetime

A timestamp in RFC 3339 format

external\_id: Optional[str]

List User Profiles

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.user_profiles.list()
page = page.data[0]
print(page.id)
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "metadata": {
        "foo": "string"
      },
      "trust_grants": {
        "foo": {
          "status": "status"
        }
      },
      "type": "type",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "external_id": "external_id"
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
      "created_at": "2019-12-27T18:11:19.117Z",
      "metadata": {
        "foo": "string"
      },
      "trust_grants": {
        "foo": {
          "status": "status"
        }
      },
      "type": "type",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "external_id": "external_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
