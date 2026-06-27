# Models

Copy page



C#

# Models

##### [List Models](api/beta/models/list.md)

[ModelListPageResponse](api/beta/models.md) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta/models.md) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



class BetaCapabilitySupport:

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



class BetaContextManagementCapability:

Context management capability details.

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

class BetaEffortCapability:

Effort (reasoning\_effort) capability details.

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

class BetaModelCapabilities:

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



class BetaThinkingCapability:

Thinking capability details.

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



class BetaThinkingTypes:

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

---

*Copyright © Anthropic. All rights reserved.*
