# List User Profiles

Copy page

Go

# List User Profiles

client.Beta.UserProfiles.List(ctx, params) (\*PageCursorV2[[BetaUserProfile](api/beta.md)], error)

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

params BetaUserProfileListParams

Limit param.Field[int64]optional

Query param: Query parameter for limit

Order param.Field[[BetaUserProfileListParamsOrder](api/beta/user_profiles/list.md)]optional

Query param: Query parameter for order

const BetaUserProfileListParamsOrderAsc [BetaUserProfileListParamsOrder](api/beta/user_profiles/list.md) = "asc"

const BetaUserProfileListParamsOrderDesc [BetaUserProfileListParamsOrder](api/beta/user_profiles/list.md) = "desc"

Page param.Field[string]optional

Query param: Query parameter for page

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

##### ReturnsExpand Collapse

type BetaUserProfile struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

TrustGrants map[string, [BetaUserProfileTrustGrant](api/beta.md)]

Status string

Type string

UpdatedAt Time

A timestamp in RFC 3339 format

ExternalID stringoptional

List User Profiles

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
  page, err := client.Beta.UserProfiles.List(context.TODO(), anthropic.BetaUserProfileListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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
