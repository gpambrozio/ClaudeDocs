# Models

Copy page



cURL

# Models

##### [List Models](api/http/beta/models/list.md)

GET/v1/models

##### [Get a Model](api/http/beta/models/retrieve.md)

GET/v1/models/{model\_id}

##### Models



BetaCapabilitySupport object{ supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



BetaContextManagementCapability object{ clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.



clear\_thinking\_20251015: [BetaCapabilitySupport](api/http/beta/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/http/beta/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.



compact\_20260112: [BetaCapabilitySupport](api/http/beta/models.md) { supported } or null

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.



BetaEffortCapability object{ high, low, max, 3 more }

Effort (reasoning\_effort) capability details.



BetaModelCapabilities object{ batch, citations, code\_execution, 6 more }

Model capability information.



BetaModelInfo object{ id, allowed\_fallback\_models, capabilities, 5 more }



BetaThinkingCapability object{ supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.



types: [BetaThinkingTypes](api/http/beta/models.md) { adaptive, enabled }

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/http/beta/models.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/http/beta/models.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.



BetaThinkingTypes object{ adaptive, enabled }

Supported thinking type configurations.



adaptive: [BetaCapabilitySupport](api/http/beta/models.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.



enabled: [BetaCapabilitySupport](api/http/beta/models.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
