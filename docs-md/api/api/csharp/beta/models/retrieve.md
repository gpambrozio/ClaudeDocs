# Get a Model

Copy page



C#

# Get a Model

[BetaModelInfo](api/beta/models.md) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.

##### ParametersExpand Collapse



ModelRetrieveParams parameters

required string modelID

Model identifier or alias.



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class BetaModelInfo:

required string ID

Unique model identifier.

required IReadOnlyList<string>? AllowedFallbackModels

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.



required [BetaModelCapabilities](api/beta/models.md)? Capabilities

Model capability information.



required [BetaCapabilitySupport](api/beta/models.md) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaContextManagementCapability](api/beta/models.md) ContextManagement

Context management support and available strategies.



required [BetaCapabilitySupport](api/beta/models.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaEffortCapability](api/beta/models.md) Effort

Effort (reasoning\_effort) support and available levels.



required [BetaCapabilitySupport](api/beta/models.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md)? Xhigh

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaThinkingCapability](api/beta/models.md) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.



required [BetaThinkingTypes](api/beta/models.md) Types

Supported thinking type configurations.



required [BetaCapabilitySupport](api/beta/models.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.



required [BetaCapabilitySupport](api/beta/models.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

required Long? MaxInputTokens

Maximum input context window size in tokens for this model.

required Long? MaxTokens

Maximum value for the `max_tokens` parameter when using this model.



JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

Get a Model

C#

```shiki
ModelRetrieveParams parameters = new() { ModelID = "model_id" };

var betaModelInfo = await client.Beta.Models.Retrieve(parameters);

Console.WriteLine(betaModelInfo);
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
