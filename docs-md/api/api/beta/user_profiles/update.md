# Update User Profile

Copy page

cURL

# Update User Profile

POST/v1/user\_profiles/{id}

Update User Profile

##### Path ParametersExpand Collapse

id: string

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 19 more

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

##### Body ParametersJSONExpand Collapse

external\_id: optional string

metadata: optional map[string]

Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

##### ReturnsExpand Collapse

BetaUserProfile = object { id, created\_at, metadata, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

trust\_grants: map[[BetaUserProfileTrustGrant](api/beta.md) { status } ]

status: string

type: string

updated\_at: string

A timestamp in RFC 3339 format

external\_id: optional string

Update User Profile

cURL

```shiki
curl https://api.anthropic.com/v1/user_profiles/$ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
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
