# Get Skill

Copy page

Go

# Get Skill

client.Beta.Skills.Get(ctx, skillID, query) (\*[BetaSkillGetResponse](api/beta.md), error)

get/v1/skills/{skill\_id}

Get Skill

##### ParametersExpand Collapse

skillID string

Unique identifier for the skill.

The format and length of IDs may change over time.

query BetaSkillGetParams

Betas param.Field[[]AnthropicBeta]optional

Optional header to specify the beta version(s) you want to use.

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

##### ReturnsExpand Collapse

type BetaSkillGetResponse struct{…}

ID string

Unique identifier for the skill.

The format and length of IDs may change over time.

CreatedAt string

ISO 8601 timestamp of when the skill was created.

DisplayTitle string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

LatestVersion string

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

Source string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

Type string

Object type.

For Skills, this is always `"skill"`.

UpdatedAt string

ISO 8601 timestamp of when the skill was last updated.

Get Skill

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
  skill, err := client.Beta.Skills.Get(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
}
```

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```