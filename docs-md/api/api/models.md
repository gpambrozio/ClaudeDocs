# Models

Copy page

SDK language

cURL

# Models

##### [List Models](api/models/list.md)

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



CapabilitySupport object { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



ContextManagementCapability object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management capability details.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



EffortCapability object { high, low, max, 3 more } 

Effort (reasoning\_effort) capability details.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



ModelCapabilities object { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.



citations: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.



code\_execution: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.



context\_management: [ContextManagementCapability](api/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



effort: [EffortCapability](api/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



image\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.



pdf\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.



structured\_outputs: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.



thinking: [ThinkingCapability](api/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.



ModelInfo object { id, capabilities, created\_at, 4 more } 

id: string

Unique model identifier.



capabilities: [ModelCapabilities](api/models.md) { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.



citations: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.



code\_execution: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.



context\_management: [ContextManagementCapability](api/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



effort: [EffortCapability](api/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



image\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.



pdf\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.



structured\_outputs: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.



thinking: [ThinkingCapability](api/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

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



ThinkingCapability object { supported, types } 

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.



ThinkingTypes object { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
