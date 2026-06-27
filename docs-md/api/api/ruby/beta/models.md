# Models

Copy page



Ruby

# Models

##### [List Models](api/beta/models/list.md)

beta.models.list(\*\*kwargs) -> Page<[BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more } >

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta/models.md) { id, allowed\_fallback\_models, capabilities, 5 more }

GET/v1/models/{model\_id}

##### ModelsExpand Collapse



class BetaCapabilitySupport { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



class BetaContextManagementCapability { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management capability details.



clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



class BetaEffortCapability { high, low, max, 3 more } 

Effort (reasoning\_effort) capability details.



high: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



class BetaModelCapabilities { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.



citations: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.



code\_execution: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.



context\_management: [BetaContextManagementCapability](api/beta/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



effort: [BetaEffortCapability](api/beta/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



image\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.



pdf\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.



structured\_outputs: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.



thinking: [BetaThinkingCapability](api/beta/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.



types: [BetaThinkingTypes](api/beta/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.



class BetaModelInfo { id, allowed\_fallback\_models, capabilities, 5 more } 

id: String

Unique model identifier.

allowed\_fallback\_models: Array[String]

Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.



capabilities: [BetaModelCapabilities](api/beta/models.md) { batch, citations, code\_execution, 6 more } 

Model capability information.



batch: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.



citations: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.



code\_execution: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.



context\_management: [BetaContextManagementCapability](api/beta/models.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported } 

Context management support and available strategies.



clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



compact\_20260112: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



effort: [BetaEffortCapability](api/beta/models.md) { high, low, max, 3 more } 

Effort (reasoning\_effort) support and available levels.



high: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.



low: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.



max: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.



medium: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.



xhigh: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.



image\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.



pdf\_input: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.



structured\_outputs: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.



thinking: [BetaThinkingCapability](api/beta/models.md) { supported, types } 

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.



types: [BetaThinkingTypes](api/beta/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/beta/models.md) { supported } 

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

class BetaThinkingCapability { supported, types } 

Thinking capability details.

supported: bool

Whether this capability is supported by the model.



types: [BetaThinkingTypes](api/beta/models.md) { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.



class BetaThinkingTypes { adaptive, enabled } 

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/beta/models.md) { supported } 

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
