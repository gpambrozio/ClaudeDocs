# Models

Copy page



Ruby

# Models

##### [List Models](api/models/list.md)

models.list(\*\*kwargs) -> Page<[ModelInfo](api/models.md) { id, capabilities, created\_at, 4 more } >

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

models.retrieve(model\_id, \*\*kwargs) -> [ModelInfo](api/models.md) { id, capabilities, created\_at, 4 more }

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



class CapabilitySupport { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



class ContextManagementCapability { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management capability details.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



class EffortCapability { high, low, max, 3 more } 

Effort (reasoning\_effort) capability details.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



class ModelCapabilities { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.



citations: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.



code\_execution: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.



context\_management: [ContextManagementCapability](api/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



effort: [EffortCapability](api/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



image\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.



pdf\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.



structured\_outputs: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.



thinking: [ThinkingCapability](api/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.



class ModelInfo { id, capabilities, created\_at, 4 more } 

id: String

Unique model identifier.



capabilities: [ModelCapabilities](api/models.md) { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.



citations: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.



code\_execution: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.



context\_management: [ContextManagementCapability](api/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



effort: [EffortCapability](api/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [CapabilitySupport](api/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



image\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.



pdf\_input: [CapabilitySupport](api/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.



structured\_outputs: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.



thinking: [ThinkingCapability](api/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: String

A human-readable name for the model.

max\_input\_tokens: Integer

Maximum input context window size in tokens for this model.

max\_tokens: Integer

Maximum value for the `max_tokens` parameter when using this model.



type: :model

Object type.

For Models, this is always `"model"`.



class ThinkingCapability { supported, types } 

Thinking capability details.

supported: bool

Whether this capability is supported by the model.



types: [ThinkingTypes](api/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.



class ThinkingTypes { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
