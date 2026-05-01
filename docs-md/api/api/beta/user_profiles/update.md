# Update User Profile

Copy page

cURL

# Update User Profile

POST/v1/user\_profiles/{user\_profile\_id}

Update User Profile

##### Path ParametersExpand Collapse

user\_profile\_id: string

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 20 more

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

##### Body ParametersJSONExpand Collapse

external\_id: optional string

If present, replaces the stored external\_id. Omit to leave unchanged. Maximum 255 characters.

metadata: optional map[string]

Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

##### ReturnsExpand Collapse

BetaUserProfile = object { id, created\_at, metadata, 4 more }

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

trust\_grants: map[[BetaUserProfileTrustGrant](api/beta.md) { status } ]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

status: "active" or "pending" or "rejected"

Status of the trust grant.

Accepts one of the following:

"active"

"pending"

"rejected"

type: "user\_profile"

Object type. Always `user_profile`.

updated\_at: string

A timestamp in RFC 3339 format

external\_id: optional string

Platform's own identifier for this user. Not enforced unique.

Update User Profile

cURL

```shiki
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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
