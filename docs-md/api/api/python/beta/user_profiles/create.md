# Create User Profile

Copy page

Python

# Create User Profile

beta.user\_profiles.create(UserProfileCreateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles

Create User Profile

##### ParametersExpand Collapse

external\_id: Optional[str]

Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

metadata: Optional[Dict[str, str]]

Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

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

class BetaUserProfile: …

id: str

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: datetime

A timestamp in RFC 3339 format

metadata: Dict[str, str]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

trust\_grants: Dict[str, [BetaUserProfileTrustGrant](api/beta.md)]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

status: Literal["active", "pending", "rejected"]

Status of the trust grant.

Accepts one of the following:

"active"

"pending"

"rejected"

type: Literal["user\_profile"]

Object type. Always `user_profile`.

updated\_at: datetime

A timestamp in RFC 3339 format

external\_id: Optional[str]

Platform's own identifier for this user. Not enforced unique.

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
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345"
}
```

---

*Copyright © Anthropic. All rights reserved.*
