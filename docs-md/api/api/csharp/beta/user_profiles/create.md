# Create User Profile

Copy page

C#

# Create User Profile

[BetaUserProfile](api/beta.md) Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles

Create User Profile

##### ParametersExpand Collapse

UserProfileCreateParams parameters

string? externalID

Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

IReadOnlyDictionary<string, string> metadata

Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

##### ReturnsExpand Collapse

class BetaUserProfile:

required string ID

Unique identifier for this user profile, prefixed `uprof_`.

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

required IReadOnlyDictionary<string, [BetaUserProfileTrustGrant](api/beta.md)> TrustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

required Status Status

Status of the trust grant.

Accepts one of the following:

"active"Active

"pending"Pending

"rejected"Rejected

required Type Type

Object type. Always `user_profile`.

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? ExternalID

Platform's own identifier for this user. Not enforced unique.

Create User Profile

C#

```shiki
UserProfileCreateParams parameters = new();

var betaUserProfile = await client.Beta.UserProfiles.Create(parameters);

Console.WriteLine(betaUserProfile);
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
