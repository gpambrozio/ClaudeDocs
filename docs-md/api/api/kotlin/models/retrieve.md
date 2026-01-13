# Get a Model

Copy page

Kotlin

# Get a Model

models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [ModelInfo](api/models.md)

get/v1/models/{model\_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse

params: ModelRetrieveParams

modelId: Optional<String>

Model identifier or alias.

betas: Optional<List<AnthropicBeta>>

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

##### ReturnsExpand Collapse

class ModelInfo:

id: String

Unique model identifier.

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

displayName: String

A human-readable name for the model.

type: JsonValue; "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

MODEL("model")

Get a Model

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.models.ModelInfo
import com.anthropic.models.models.ModelRetrieveParams

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val modelInfo: ModelInfo = client.models().retrieve("model_id")
}
```

Response 200

```shiki
{
  "id": "claude-sonnet-4-20250514",
  "created_at": "2025-02-19T00:00:00Z",
  "display_name": "Claude Sonnet 4",
  "type": "model"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "claude-sonnet-4-20250514",
  "created_at": "2025-02-19T00:00:00Z",
  "display_name": "Claude Sonnet 4",
  "type": "model"
}
```