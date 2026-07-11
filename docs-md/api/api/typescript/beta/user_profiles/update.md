# Update User Profile

Copy page



TypeScript

# Update User Profile

client.beta.userProfiles.update(stringuserProfileID, UserProfileUpdateParams { external\_id, metadata, name, 2 more } params, RequestOptionsoptions?): [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more }

POST/v1/user\_profiles/{user\_profile\_id}

Update User Profile

##### ParametersExpand Collapse

userProfileID: string



params: UserProfileUpdateParams { external\_id, metadata, name, 2 more } 

external\_id?: string | null

Body param: If present, replaces the stored external\_id. Omit to leave unchanged. Maximum 255 characters.

metadata?: Record<string, string>

Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

name?: string | null

Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.



relationship?: "external" | "resold" | "internal" | null

Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

One of the following:

"external"

"resold"

"internal"



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 26 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



BetaUserProfile { id, created\_at, metadata, 6 more } 

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



relationship: "external" | "resold" | "internal"

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

One of the following:

"external"

"resold"

"internal"



trust\_grants: Record<string, [BetaUserProfileTrustGrant](api/beta/user_profiles.md) { status } >

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: "active" | "pending" | "rejected"

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

type: "user\_profile"

Object type. Always `user_profile`.

updated\_at: string

A timestamp in RFC 3339 format

external\_id?: string | null

Platform's own identifier for this user. Not enforced unique.

name?: string | null

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

Update User Profile

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaUserProfile = await client.beta.userProfiles.update('uprof_011CZkZCu8hGbp5mYRQgUmz9');

console.log(betaUserProfile.id);
```

Response 200



```shiki
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

---

*Copyright © Anthropic. All rights reserved.*
