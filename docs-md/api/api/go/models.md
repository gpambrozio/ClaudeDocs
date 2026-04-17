# Models

Copy page

Go

# Models

##### [List Models](api/models/list.md)

client.Models.List(ctx, params) (\*Page[[ModelInfo](api/models.md)], error)

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

client.Models.Get(ctx, modelID, query) (\*[ModelInfo](api/models.md), error)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

type CapabilitySupport struct{…}

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type ContextManagementCapability struct{…}

Context management capability details.

ClearThinking20251015 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

type EffortCapability struct{…}

Effort (reasoning\_effort) capability details.

High [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

type ModelCapabilities struct{…}

Model capability information.

Batch [CapabilitySupport](api/models.md)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [CapabilitySupport](api/models.md)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [CapabilitySupport](api/models.md)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [ContextManagementCapability](api/models.md)

Context management support and available strategies.

ClearThinking20251015 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [EffortCapability](api/models.md)

Effort (reasoning\_effort) support and available levels.

High [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ImageInput [CapabilitySupport](api/models.md)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [CapabilitySupport](api/models.md)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [CapabilitySupport](api/models.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [ThinkingCapability](api/models.md)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](api/models.md)

Supported thinking type configurations.

Adaptive [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type ModelInfo struct{…}

ID string

Unique model identifier.

Capabilities [ModelCapabilities](api/models.md)

Model capability information.

Batch [CapabilitySupport](api/models.md)

Whether the model supports the Batch API.

Supported bool

Whether this capability is supported by the model.

Citations [CapabilitySupport](api/models.md)

Whether the model supports citation generation.

Supported bool

Whether this capability is supported by the model.

CodeExecution [CapabilitySupport](api/models.md)

Whether the model supports code execution tools.

Supported bool

Whether this capability is supported by the model.

ContextManagement [ContextManagementCapability](api/models.md)

Context management support and available strategies.

ClearThinking20251015 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ClearToolUses20250919 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Compact20260112 [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Effort [EffortCapability](api/models.md)

Effort (reasoning\_effort) support and available levels.

High [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

Supported bool

Whether this capability is supported by the model.

Low [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

Supported bool

Whether this capability is supported by the model.

Max [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

Supported bool

Whether this capability is supported by the model.

Medium [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

Supported bool

Whether this capability is supported by the model.

Supported bool

Whether this capability is supported by the model.

Xhigh [CapabilitySupport](api/models.md)

Indicates whether a capability is supported.

Supported bool

Whether this capability is supported by the model.

ImageInput [CapabilitySupport](api/models.md)

Whether the model accepts image content blocks.

Supported bool

Whether this capability is supported by the model.

PDFInput [CapabilitySupport](api/models.md)

Whether the model accepts PDF content blocks.

Supported bool

Whether this capability is supported by the model.

StructuredOutputs [CapabilitySupport](api/models.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

Supported bool

Whether this capability is supported by the model.

Thinking [ThinkingCapability](api/models.md)

Thinking capability and supported type configurations.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](api/models.md)

Supported thinking type configurations.

Adaptive [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](api/models.md)

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

type ThinkingCapability struct{…}

Thinking capability details.

Supported bool

Whether this capability is supported by the model.

Types [ThinkingTypes](api/models.md)

Supported thinking type configurations.

Adaptive [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

type ThinkingTypes struct{…}

Supported thinking type configurations.

Adaptive [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

Supported bool

Whether this capability is supported by the model.

Enabled [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

Supported bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
