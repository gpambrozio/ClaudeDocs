# Models

Copy page



PHP

# Models

##### [List Models](api/models/list.md)

$client->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[ModelInfo](api/models.md)>

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

$client->models->retrieve(string modelID, ?list<AnthropicBeta> betas): [ModelInfo](api/models.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



[CapabilitySupport](api/models.md)

bool supported

Whether this capability is supported by the model.



[ContextManagementCapability](api/models.md)

?[CapabilitySupport](api/models.md) clearThinking20251015

Indicates whether a capability is supported.

?[CapabilitySupport](api/models.md) clearToolUses20250919

Indicates whether a capability is supported.

?[CapabilitySupport](api/models.md) compact20260112

Indicates whether a capability is supported.

bool supported

Whether this capability is supported by the model.



[EffortCapability](api/models.md)

[CapabilitySupport](api/models.md) high

Whether the model supports high effort level.

[CapabilitySupport](api/models.md) low

Whether the model supports low effort level.

[CapabilitySupport](api/models.md) max

Whether the model supports max effort level.

[CapabilitySupport](api/models.md) medium

Whether the model supports medium effort level.

bool supported

Whether this capability is supported by the model.

?[CapabilitySupport](api/models.md) xhigh

Indicates whether a capability is supported.



[ModelCapabilities](api/models.md)

[CapabilitySupport](api/models.md) batch

Whether the model supports the Batch API.

[CapabilitySupport](api/models.md) citations

Whether the model supports citation generation.

[CapabilitySupport](api/models.md) codeExecution

Whether the model supports code execution tools.

[ContextManagementCapability](api/models.md) contextManagement

Context management support and available strategies.

[EffortCapability](api/models.md) effort

Effort (reasoning\_effort) support and available levels.

[CapabilitySupport](api/models.md) imageInput

Whether the model accepts image content blocks.

[CapabilitySupport](api/models.md) pdfInput

Whether the model accepts PDF content blocks.

[CapabilitySupport](api/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

[ThinkingCapability](api/models.md) thinking

Thinking capability and supported type configurations.



[ModelInfo](api/models.md)

string id

Unique model identifier.

?[ModelCapabilities](api/models.md) capabilities

Model capability information.

\Datetime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

string displayName

A human-readable name for the model.

?int maxInputTokens

Maximum input context window size in tokens for this model.

?int maxTokens

Maximum value for the `max_tokens` parameter when using this model.



"model" type

Object type.

For Models, this is always `"model"`.



[ThinkingCapability](api/models.md)

bool supported

Whether this capability is supported by the model.

[ThinkingTypes](api/models.md) types

Supported thinking type configurations.



[ThinkingTypes](api/models.md)

[CapabilitySupport](api/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

[CapabilitySupport](api/models.md) enabled

Whether the model supports thinking with type 'enabled'.

---

*Copyright © Anthropic. All rights reserved.*
