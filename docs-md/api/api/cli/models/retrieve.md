# Get a Model

Copy page



CLI

# Get a Model

$ ant models retrieve

GET/v1/models/{model\_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse

--model-id: string

Model identifier or alias.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



model\_info: object { id, capabilities, created\_at, 4 more } 

id: string

Unique model identifier.



capabilities: object { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: object { supported } 

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.



citations: object { supported } 

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.



code\_execution: object { supported } 

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.



context\_management: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: object { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: object { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: object { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



effort: object { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: object { supported } 

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.



low: object { supported } 

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.



max: object { supported } 

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.



medium: object { supported } 

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



xhigh: object { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



image\_input: object { supported } 

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.



pdf\_input: object { supported } 

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.



structured\_outputs: object { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.



thinking: object { supported, types } 

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.



types: object { adaptive, enabled } 

Supported thinking type configurations.



adaptive: object { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: object { supported } 

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

max\_input\_tokens: number

Maximum input context window size in tokens for this model.

max\_tokens: number

Maximum value for the `max_tokens` parameter when using this model.



type: "model"

Object type.

For Models, this is always `"model"`.

Get a Model

CLI

```shiki
ant models retrieve \
  --api-key my-anthropic-api-key \
  --model-id model_id
```

Response 200



```shiki
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
