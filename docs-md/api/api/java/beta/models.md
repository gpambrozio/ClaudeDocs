# Models

Copy page



Java

# Models

##### [List Models](api/beta/models/list.md)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta/models.md) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



class BetaCapabilitySupport:

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



class BetaContextManagementCapability:

Context management capability details.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



class BetaEffortCapability:

Effort (reasoning\_effort) capability details.



[BetaCapabilitySupport](api/beta/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



class BetaModelCapabilities:

Model capability information.



[BetaCapabilitySupport](api/beta/models.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.



[BetaContextManagementCapability](api/beta/models.md) contextManagement

Context management support and available strategies.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



[BetaEffortCapability](api/beta/models.md) effort

Effort (reasoning\_effort) support and available levels.



[BetaCapabilitySupport](api/beta/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.



[BetaThinkingCapability](api/beta/models.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.



[BetaThinkingTypes](api/beta/models.md) types

Supported thinking type configurations.



[BetaCapabilitySupport](api/beta/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.



class BetaModelInfo:

String id

Unique model identifier.

Optional<List<String>> allowedFallbackModels

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.



Optional<[BetaModelCapabilities](api/beta/models.md)> capabilities

Model capability information.



[BetaCapabilitySupport](api/beta/models.md) batch

Whether the model supports the Batch API.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) citations

Whether the model supports citation generation.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) codeExecution

Whether the model supports code execution tools.

boolean supported

Whether this capability is supported by the model.



[BetaContextManagementCapability](api/beta/models.md) contextManagement

Context management support and available strategies.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearThinking20251015

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> clearToolUses20250919

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> compact20260112

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



[BetaEffortCapability](api/beta/models.md) effort

Effort (reasoning\_effort) support and available levels.



[BetaCapabilitySupport](api/beta/models.md) high

Whether the model supports high effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) low

Whether the model supports low effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) max

Whether the model supports max effort level.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) medium

Whether the model supports medium effort level.

boolean supported

Whether this capability is supported by the model.

boolean supported

Whether this capability is supported by the model.



Optional<[BetaCapabilitySupport](api/beta/models.md)> xhigh

Indicates whether a capability is supported.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) imageInput

Whether the model accepts image content blocks.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) pdfInput

Whether the model accepts PDF content blocks.

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

boolean supported

Whether this capability is supported by the model.



[BetaThinkingCapability](api/beta/models.md) thinking

Thinking capability and supported type configurations.

boolean supported

Whether this capability is supported by the model.



[BetaThinkingTypes](api/beta/models.md) types

Supported thinking type configurations.



[BetaCapabilitySupport](api/beta/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

Optional<Long> maxInputTokens

Maximum input context window size in tokens for this model.

Optional<Long> maxTokens

Maximum value for the `max_tokens` parameter when using this model.



JsonValue; type "model"constant"model"constant

Object type.

For Models, this is always `"model"`.



class BetaThinkingCapability:

Thinking capability details.

boolean supported

Whether this capability is supported by the model.



[BetaThinkingTypes](api/beta/models.md) types

Supported thinking type configurations.



[BetaCapabilitySupport](api/beta/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.



class BetaThinkingTypes:

Supported thinking type configurations.



[BetaCapabilitySupport](api/beta/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

boolean supported

Whether this capability is supported by the model.



[BetaCapabilitySupport](api/beta/models.md) enabled

Whether the model supports thinking with type 'enabled'.

boolean supported

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
