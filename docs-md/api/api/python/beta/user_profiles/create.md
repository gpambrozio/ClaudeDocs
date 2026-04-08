# Create User Profile

Copy page

Python

# Create User Profile

beta.user\_profiles.create(UserProfileCreateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles

Create User Profile

##### ParametersExpand Collapse

external\_id: Optional[str]

metadata: Optional[Dict[str, str]]

Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

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

Create User Profile

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.create()
print(beta_user_profile.id)
```

Response 200

```shiki
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
```

##### Returns Examples

Response 200

```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
