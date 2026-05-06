# Update User Profile

Copy page

Go

# Update User Profile

client.Beta.UserProfiles.Update(ctx, userProfileID, params) (\*[BetaUserProfile](api/beta.md), error)

POST/v1/user\_profiles/{user\_profile\_id}

Update User Profile

##### ParametersExpand Collapse

userProfileID string

params BetaUserProfileUpdateParams

ExternalID param.Field[string]optional

Body param: If present, replaces the stored external\_id. Omit to leave unchanged. Maximum 255 characters.

Metadata param.Field[map[string, string]]optional

Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

Name param.Field[string]optional

Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

Relationship param.Field[[BetaUserProfileUpdateParamsRelationship](api/beta/user_profiles/update.md)]optional

Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

const BetaUserProfileUpdateParamsRelationshipExternal [BetaUserProfileUpdateParamsRelationship](api/beta/user_profiles/update.md) = "external"

const BetaUserProfileUpdateParamsRelationshipResold [BetaUserProfileUpdateParamsRelationship](api/beta/user_profiles/update.md) = "resold"

const BetaUserProfileUpdateParamsRelationshipInternal [BetaUserProfileUpdateParamsRelationship](api/beta/user_profiles/update.md) = "internal"

Betas param.Field[[]AnthropicBeta]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

##### ReturnsExpand Collapse

type BetaUserProfile struct{…}

ID string

Unique identifier for this user profile, prefixed `uprof_`.

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship BetaUserProfileRelationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

Accepts one of the following:

const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"

const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"

const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"

TrustGrants map[string, [BetaUserProfileTrustGrant](api/beta.md)]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Status BetaUserProfileTrustGrantStatus

Status of the trust grant.

Accepts one of the following:

const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"

const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"

const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"

Type BetaUserProfileType

Object type. Always `user_profile`.

UpdatedAt Time

A timestamp in RFC 3339 format

ExternalID stringoptional

Platform's own identifier for this user. Not enforced unique.

Name stringoptional

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

Update User Profile

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaUserProfile, err := client.Beta.UserProfiles.Update(
    context.TODO(),
    "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    anthropic.BetaUserProfileUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaUserProfile.ID)
}
```

Response 200

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
