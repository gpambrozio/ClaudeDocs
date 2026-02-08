# Get a Model

Copy page

Go

# Get a Model

client.Beta.Models.Get(ctx, modelID, query) (\*[BetaModelInfo](api/beta.md), error)

get/v1/models/{model\_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse

modelID string

Model identifier or alias.

query BetaModelGetParams

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

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

##### ReturnsExpand Collapse

type BetaModelInfo struct{…}

ID string

Unique model identifier.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

DisplayName string

A human-readable name for the model.

Type Model

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

const ModelModel Model = "model"

Get a Model

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
  betaModelInfo, err := client.Beta.Models.Get(
    context.TODO(),
    "model_id",
    anthropic.BetaModelGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaModelInfo.ID)
}
```

Response 200

```shiki
{
  "id": "claude-opus-4-6",
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "type": "model"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "claude-opus-4-6",
  "created_at": "2026-02-04T00:00:00Z",
  "display_name": "Claude Opus 4.6",
  "type": "model"
}
```

---

*Copyright © Anthropic. All rights reserved.*
