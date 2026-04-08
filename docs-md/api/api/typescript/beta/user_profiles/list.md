# List User Profiles

Copy page

TypeScript

# List User Profiles

client.beta.userProfiles.list(UserProfileListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursorV2<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

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

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more

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

BetaUserProfile { id, created\_at, metadata, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

trust\_grants: Record<string, [BetaUserProfileTrustGrant](api/beta.md) { status } >

status: string

type: string

updated\_at: string

A timestamp in RFC 3339 format

external\_id?: string | null

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
