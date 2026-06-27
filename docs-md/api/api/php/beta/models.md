# Models

Copy page



PHP

# Models

##### [List Models](api/beta/models/list.md)

$client->beta->models->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas): Page<[BetaModelInfo](api/beta/models.md)>

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

$client->beta->models->retrieve(string modelID, ?list<AnthropicBeta> betas): [BetaModelInfo](api/beta/models.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



[BetaCapabilitySupport](api/beta/models.md)

bool supported

Whether this capability is supported by the model.



[BetaContextManagementCapability](api/beta/models.md)

?[BetaCapabilitySupport](api/beta/models.md) clearThinking20251015

Indicates whether a capability is supported.

?[BetaCapabilitySupport](api/beta/models.md) clearToolUses20250919

Indicates whether a capability is supported.

?[BetaCapabilitySupport](api/beta/models.md) compact20260112

Indicates whether a capability is supported.

bool supported

Whether this capability is supported by the model.



[BetaEffortCapability](api/beta/models.md)

[BetaCapabilitySupport](api/beta/models.md) high

Whether the model supports high effort level.

[BetaCapabilitySupport](api/beta/models.md) low

Whether the model supports low effort level.

[BetaCapabilitySupport](api/beta/models.md) max

Whether the model supports max effort level.

[BetaCapabilitySupport](api/beta/models.md) medium

Whether the model supports medium effort level.

bool supported

Whether this capability is supported by the model.

?[BetaCapabilitySupport](api/beta/models.md) xhigh

Indicates whether a capability is supported.



[BetaModelCapabilities](api/beta/models.md)

[BetaCapabilitySupport](api/beta/models.md) batch

Whether the model supports the Batch API.

[BetaCapabilitySupport](api/beta/models.md) citations

Whether the model supports citation generation.

[BetaCapabilitySupport](api/beta/models.md) codeExecution

Whether the model supports code execution tools.

[BetaContextManagementCapability](api/beta/models.md) contextManagement

Context management support and available strategies.

[BetaEffortCapability](api/beta/models.md) effort

Effort (reasoning\_effort) support and available levels.

[BetaCapabilitySupport](api/beta/models.md) imageInput

Whether the model accepts image content blocks.

[BetaCapabilitySupport](api/beta/models.md) pdfInput

Whether the model accepts PDF content blocks.

[BetaCapabilitySupport](api/beta/models.md) structuredOutputs

Whether the model supports structured output / JSON mode / strict tool schemas.

[BetaThinkingCapability](api/beta/models.md) thinking

Thinking capability and supported type configurations.



[BetaModelInfo](api/beta/models.md)

string id

Unique model identifier.

?list<string> allowedFallbackModels

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.

?[BetaModelCapabilities](api/beta/models.md) capabilities

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

[BetaThinkingCapability](api/beta/models.md)

bool supported

Whether this capability is supported by the model.

[BetaThinkingTypes](api/beta/models.md) types

Supported thinking type configurations.



[BetaThinkingTypes](api/beta/models.md)

[BetaCapabilitySupport](api/beta/models.md) adaptive

Whether the model supports thinking with type 'adaptive' (auto).

[BetaCapabilitySupport](api/beta/models.md) enabled

Whether the model supports thinking with type 'enabled'.

---

*Copyright © Anthropic. All rights reserved.*
