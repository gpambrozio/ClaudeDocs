# List Skill Versions

Copy page

Go

# List Skill Versions

client.Beta.Skills.Versions.List(ctx, skillID, params) (\*PageCursor[[BetaSkillVersionListResponse](api/beta.md)], error)

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### ParametersExpand Collapse

skillID string

Unique identifier for the skill.

The format and length of IDs may change over time.

params BetaSkillVersionListParams

Limit param.Field[int64]optional

Query param: Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

Page param.Field[string]optional

Query param: Optionally set to the `next_page` token from the previous response.

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

##### ReturnsExpand Collapse

type BetaSkillVersionListResponse struct{…}

ID string

Unique identifier for the skill version.

The format and length of IDs may change over time.

CreatedAt string

ISO 8601 timestamp of when the skill version was created.

Description string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

Directory string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

Name string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

SkillID string

Identifier for the skill that this version belongs to.

Type string

Object type.

For Skill Versions, this is always `"skill_version"`.

Version string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

List Skill Versions

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
  page, err := client.Beta.Skills.Versions.List(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillVersionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
}
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
