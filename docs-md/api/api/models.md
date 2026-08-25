# Models

Copy page



cURL

# Models

##### [List Models](api/http/models/list.md)

GET/v1/models

##### [Get a Model](api/http/models/retrieve.md)

GET/v1/models/{model\_id}

##### Models



CapabilitySupport object{ supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



ContextManagementCapability object{ clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.



clear\_thinking\_20251015: [CapabilitySupport](api/http/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [CapabilitySupport](api/http/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: [CapabilitySupport](api/http/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



EffortCapability object{ high, low, max, 3 more }

Effort (reasoning\_effort) capability details.



ModelCapabilities object{ batch, citations, code\_execution, 6 more }

Model capability information.



ModelInfo object{ id, capabilities, created\_at, 4 more }

id: string

Unique model identifier.



capabilities: [ModelCapabilities](api/http/models.md) { batch, citations, code\_execution, 6 more } or null

Model capability information.



created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: string

A human-readable name for the model.

max\_input\_tokens: number or null

Maximum input context window size in tokens for this model.

max\_tokens: number or null

Maximum value for the `max_tokens` parameter when using this model.



type: "model"

Object type.

For Models, this is always `"model"`.

defaultmodel



ThinkingCapability object{ supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.



types: [ThinkingTypes](api/http/models.md) { adaptive, enabled }

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/http/models.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/http/models.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.



ThinkingTypes object{ adaptive, enabled }

Supported thinking type configurations.



adaptive: [CapabilitySupport](api/http/models.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [CapabilitySupport](api/http/models.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
