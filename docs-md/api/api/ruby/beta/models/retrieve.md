# Get a Model

Copy page



Ruby

# Get a Model

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more }

GET/v1/models/{model\_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse

model\_id: String

Model identifier or alias.



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

:"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class BetaModelInfo { id, allowed\_fallback\_models, capabilities, 5 more } 

id: String

Unique model identifier.

allowed\_fallback\_models: Array[String]

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.



capabilities: [BetaModelCapabilities](api/beta/models.md) { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.



citations: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.



code\_execution: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.



context\_management: [BetaContextManagementCapability](api/beta/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



effort: [BetaEffortCapability](api/beta/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



image\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.



pdf\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.



structured\_outputs: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.



thinking: [BetaThinkingCapability](api/beta/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.



types: [BetaThinkingTypes](api/beta/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: String

A human-readable name for the model.

max\_input\_tokens: Integer

Maximum input context window size in tokens for this model.

max\_tokens: Integer

Maximum value for the `max_tokens` parameter when using this model.



type: :model

Object type.

For Models, this is always `"model"`.

Get a Model

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_model_info = anthropic.beta.models.retrieve("model_id")

puts(beta_model_info)
```

Response 200



```shiki
{
  "id": "claude-opus-4-6",
  "allowed_fallback_models": [
    "string"
  ],
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
      "supported": true,
      "xhigh": {
        "supported": true
      }
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
```

##### Returns Examples

Response 200



```shiki
{
  "id": "claude-opus-4-6",
  "allowed_fallback_models": [
    "string"
  ],
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
      "supported": true,
      "xhigh": {
        "supported": true
      }
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
```

---

*Copyright © Anthropic. All rights reserved.*
