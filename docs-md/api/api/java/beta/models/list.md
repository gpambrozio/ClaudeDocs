# List Models

Copy page

Java

# List Models

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.

##### ParametersExpand Collapse

ModelListParams params

Optional<String> afterId

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

Optional<String> beforeId

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

Optional<Long> limit

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

Optional<List<AnthropicBeta>> betas

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

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

##### ReturnsExpand Collapse

class BetaModelInfo:

String id

Unique model identifier.

Optional<[BetaModelCapabilities](api/beta.md)> capabilities

Model capability information.

[BetaCapabilitySupport](api/beta.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[BetaContextManagementCapability](api/beta.md) contextManagement

Context management support and available strategies.

Optional<[BetaCapabilitySupport](api/beta.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[BetaCapabilitySupport](api/beta.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaEffortCapability](api/beta.md) effort

Effort (reasoning\_effort) support and available levels.

[BetaCapabilitySupport](api/beta.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingCapability](api/beta.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta.md) types

Supported thinking type configurations.

[BetaCapabilitySupport](api/beta.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[BetaCapabilitySupport](api/beta.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

Optional<Long> maxInputTokens

Maximum input context window size in tokens for this model.

Optional<Long> maxTokens

Maximum value for the `max_tokens` parameter when using this model.

JsonValue; type "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

List Models

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.models.ModelListPage;
import com.anthropic.models.beta.models.ModelListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ModelListPage page = client.beta().models().list();
    }
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "capabilities": {
        "batch": {
          "supported": true
        },
        "citations": {
          "supported": true
        },
        "code_execution": {
          "supported": true
        },
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          },
          "clear_tool_uses_20250919": {
            "supported": true
          },
          "compact_20260112": {
            "supported": true
          },
          "supported": true
        },
        "effort": {
          "high": {
            "supported": true
          },
          "low": {
            "supported": true
          },
          "max": {
            "supported": true
          },
          "medium": {
            "supported": true
          },
          "supported": true
        },
        "image_input": {
          "supported": true
        },
        "pdf_input": {
          "supported": true
        },
        "structured_outputs": {
          "supported": true
        },
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            },
            "enabled": {
              "supported": true
            }
          }
        }
      },
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "claude-opus-4-6",
      "capabilities": {
        "batch": {
          "supported": true
        },
        "citations": {
          "supported": true
        },
        "code_execution": {
          "supported": true
        },
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          },
          "clear_tool_uses_20250919": {
            "supported": true
          },
          "compact_20260112": {
            "supported": true
          },
          "supported": true
        },
        "effort": {
          "high": {
            "supported": true
          },
          "low": {
            "supported": true
          },
          "max": {
            "supported": true
          },
          "medium": {
            "supported": true
          },
          "supported": true
        },
        "image_input": {
          "supported": true
        },
        "pdf_input": {
          "supported": true
        },
        "structured_outputs": {
          "supported": true
        },
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            },
            "enabled": {
              "supported": true
            }
          }
        }
      },
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "type": "model"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

---

*Copyright © Anthropic. All rights reserved.*
