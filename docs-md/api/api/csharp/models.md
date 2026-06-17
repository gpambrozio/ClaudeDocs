# Models

Copy page



C#

# Models

##### [List Models](api/models/list.md)

[ModelListPageResponse](api/models.md) Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

[ModelInfo](api/models.md) Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



class CapabilitySupport:

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



class ContextManagementCapability:

Context management capability details.



required [CapabilitySupport](api/models.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



class EffortCapability:

Effort (reasoning\_effort) capability details.



required [CapabilitySupport](api/models.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Xhigh

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



class ModelCapabilities:

Model capability information.



required [CapabilitySupport](api/models.md) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.



required [ContextManagementCapability](api/models.md) ContextManagement

Context management support and available strategies.



required [CapabilitySupport](api/models.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [EffortCapability](api/models.md) Effort

Effort (reasoning\_effort) support and available levels.



required [CapabilitySupport](api/models.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Xhigh

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.



required [ThinkingCapability](api/models.md) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.



required [ThinkingTypes](api/models.md) Types

Supported thinking type configurations.



required [CapabilitySupport](api/models.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.



class ModelInfo:

required string ID

Unique model identifier.



required [ModelCapabilities](api/models.md)? Capabilities

Model capability information.



required [CapabilitySupport](api/models.md) Batch

Whether the model supports the Batch API.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Citations

Whether the model supports citation generation.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) CodeExecution

Whether the model supports code execution tools.

required Boolean Supported

Whether this capability is supported by the model.



required [ContextManagementCapability](api/models.md) ContextManagement

Context management support and available strategies.



required [CapabilitySupport](api/models.md)? ClearThinking20251015

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? ClearToolUses20250919

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Compact20260112

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [EffortCapability](api/models.md) Effort

Effort (reasoning\_effort) support and available levels.



required [CapabilitySupport](api/models.md) High

Whether the model supports high effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Low

Whether the model supports low effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Max

Whether the model supports max effort level.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Medium

Whether the model supports medium effort level.

required Boolean Supported

Whether this capability is supported by the model.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md)? Xhigh

Indicates whether a capability is supported.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) ImageInput

Whether the model accepts image content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) PdfInput

Whether the model accepts PDF content blocks.

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) StructuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

required Boolean Supported

Whether this capability is supported by the model.



required [ThinkingCapability](api/models.md) Thinking

Thinking capability and supported type configurations.

required Boolean Supported

Whether this capability is supported by the model.



required [ThinkingTypes](api/models.md) Types

Supported thinking type configurations.



required [CapabilitySupport](api/models.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Enabled

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

class ThinkingCapability:

Thinking capability details.

required Boolean Supported

Whether this capability is supported by the model.



required [ThinkingTypes](api/models.md) Types

Supported thinking type configurations.



required [CapabilitySupport](api/models.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.



class ThinkingTypes:

Supported thinking type configurations.



required [CapabilitySupport](api/models.md) Adaptive

Whether the model supports thinking with type 'adaptive' (auto).

required Boolean Supported

Whether this capability is supported by the model.



required [CapabilitySupport](api/models.md) Enabled

Whether the model supports thinking with type 'enabled'.

required Boolean Supported

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
