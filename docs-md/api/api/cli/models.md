# Models

Copy page

CLI

# Models

##### [List Models](api/models/list.md)

$ ant models list

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

$ ant models retrieve

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

capability\_support: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

context\_management\_capability: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort\_capability: object { high, low, max, 3 more }

Effort (reasoning\_effort) capability details.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

model\_capabilities: object { batch, citations, code\_execution, 6 more }

Model capability information.

batch: object { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: object { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: object { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: object { high, low, max, 3 more }

Effort (reasoning\_effort) support and available levels.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

image\_input: object { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: object { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: object { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: object { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

model\_info: object { id, capabilities, created\_at, 4 more }

id: string

Unique model identifier.

capabilities: object { batch, citations, code\_execution, 6 more }

Model capability information.

batch: object { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: object { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: object { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: object { high, low, max, 3 more }

Effort (reasoning\_effort) support and available levels.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

xhigh: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

image\_input: object { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: object { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: object { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: object { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

max\_input\_tokens: number

Maximum input context window size in tokens for this model.

max\_tokens: number

Maximum value for the `max_tokens` parameter when using this model.

type: "model"

Object type.

For Models, this is always `"model"`.

thinking\_capability: object { supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

thinking\_types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
