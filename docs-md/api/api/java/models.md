# Models

Copy page

Java

# Models

##### [List Models](api/models/list.md)

ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

[ModelInfo](api/models.md) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class CapabilitySupport:

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class ContextManagementCapability:

Context management capability details.

Optional<[CapabilitySupport](api/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

class EffortCapability:

Effort (reasoning\_effort) capability details.

[CapabilitySupport](api/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

class ModelCapabilities:

Model capability information.

[CapabilitySupport](api/models.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[ContextManagementCapability](api/models.md) contextManagement

Context management support and available strategies.

Optional<[CapabilitySupport](api/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[EffortCapability](api/models.md) effort

Effort (reasoning\_effort) support and available levels.

[CapabilitySupport](api/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[ThinkingCapability](api/models.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](api/models.md) types

Supported thinking type configurations.

[CapabilitySupport](api/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class ModelInfo:

String id

Unique model identifier.

Optional<[ModelCapabilities](api/models.md)> capabilities

Model capability information.

[CapabilitySupport](api/models.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.

[ContextManagementCapability](api/models.md) contextManagement

Context management support and available strategies.

Optional<[CapabilitySupport](api/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

[EffortCapability](api/models.md) effort

Effort (reasoning\_effort) support and available levels.

[CapabilitySupport](api/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.

Optional<[CapabilitySupport](api/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.

[ThinkingCapability](api/models.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](api/models.md) types

Supported thinking type configurations.

[CapabilitySupport](api/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) enabled

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

class ThinkingCapability:

Thinking capability details.

boolean supported

Whether this capability is supported by the model.

[ThinkingTypes](api/models.md) types

Supported thinking type configurations.

[CapabilitySupport](api/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

class ThinkingTypes:

Supported thinking type configurations.

[CapabilitySupport](api/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.

[CapabilitySupport](api/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
