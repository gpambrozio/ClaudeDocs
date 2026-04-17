# List User Profiles

Copy page

TypeScript

# List User Profiles

client.beta.userProfiles.list(UserProfileListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

params: UserProfileListParams { limit, order, page, betas }

limit?: number

Query param: Query parameter for limit

order?: "asc" | "desc"

Query param: Query parameter for order

Accepts one of the following:

"asc"

"desc"

page?: string

Query param: Query parameter for page

betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 20 more

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

"user-profiles-2026-03-24"

##### ReturnsExpand Collapse

BetaUserProfile { id, created\_at, metadata, 4 more }

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

trust\_grants: Record<string, [BetaUserProfileTrustGrant](api/beta.md) { status } >

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

status: "active" | "pending" | "rejected"

Status of the trust grant.

Accepts one of the following:

"active"

"pending"

"rejected"

type: "user\_profile"

Object type. Always `user_profile`.

updated\_at: string

A timestamp in RFC 3339 format

external\_id?: string | null

Platform's own identifier for this user. Not enforced unique.

List User Profiles

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaUserProfile of client.beta.userProfiles.list()) {
  console.log(betaUserProfile.id);
}
```

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
