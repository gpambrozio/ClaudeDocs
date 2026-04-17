# Models

Copy page

Go

# Models

##### [List Models](api/beta/models/list.md)

client.Beta.Models.List(ctx, params) (\*Page[[BetaModelInfo](api/beta.md)], error)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

client.Beta.Models.Get(ctx, modelID, query) (\*[BetaModelInfo](api/beta.md), error)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

type BetaCapabilitySupport struct{…}

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type BetaContextManagementCapability struct{…}

Context management capability details.

ClearThinking20251015 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type BetaEffortCapability struct{…}

Effort (reasoning\_effort) capability details.

High [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type BetaModelCapabilities struct{…}

Model capability information.

Batch [BetaCapabilitySupport](api/beta.md)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [BetaCapabilitySupport](api/beta.md)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [BetaCapabilitySupport](api/beta.md)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [BetaContextManagementCapability](api/beta.md)

Context management support and available strategies.

ClearThinking20251015 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [BetaEffortCapability](api/beta.md)

Effort (reasoning\_effort) support and available levels.

High [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ImageInput [BetaCapabilitySupport](api/beta.md)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [BetaCapabilitySupport](api/beta.md)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [BetaCapabilitySupport](api/beta.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [BetaThinkingCapability](api/beta.md)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type BetaModelInfo struct{…}

ID string

Unique model identifier.

Capabilities [BetaModelCapabilities](api/beta.md)

Model capability information.

Batch [BetaCapabilitySupport](api/beta.md)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [BetaCapabilitySupport](api/beta.md)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [BetaCapabilitySupport](api/beta.md)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [BetaContextManagementCapability](api/beta.md)

Context management support and available strategies.

ClearThinking20251015 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [BetaEffortCapability](api/beta.md)

Effort (reasoning\_effort) support and available levels.

High [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [BetaCapabilitySupport](api/beta.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ImageInput [BetaCapabilitySupport](api/beta.md)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [BetaCapabilitySupport](api/beta.md)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [BetaCapabilitySupport](api/beta.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [BetaThinkingCapability](api/beta.md)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

DisplayName string

A human-readable name for the model.

MaxInputTokens int64

Maximum input context window size in tokens for this model.

MaxTokens int64

Maximum value for the `max_tokens` parameter when using this model.

Type Model

Object type.

For Models, this is always `"model"`.

type BetaThinkingCapability struct{…}

Thinking capability details.

Supported bool

Whether this capability is supported by the model.

Types [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type BetaThinkingTypes struct{…}

Supported thinking type configurations.

Adaptive [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
