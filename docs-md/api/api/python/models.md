# Models

Copy page

Python

# Models

##### [List Models](api/models/list.md)

models.list(ModelListParams\*\*kwargs)  -> SyncPage[[ModelInfo](api/models.md)]

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

models.retrieve(strmodel\_id, ModelRetrieveParams\*\*kwargs)  -> [ModelInfo](api/models.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class CapabilitySupport: …

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class ContextManagementCapability: …

Context management capability details.

clear\_thinking\_20251015: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class EffortCapability: …

Effort (reasoning\_effort) capability details.

high: [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class ModelCapabilities: …

Model capability information.

batch: [CapabilitySupport](api/models.md)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [CapabilitySupport](api/models.md)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [CapabilitySupport](api/models.md)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [ContextManagementCapability](api/models.md)

Context management support and available strategies.

clear\_thinking\_20251015: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [EffortCapability](api/models.md)

Effort (reasoning\_effort) support and available levels.

high: [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image\_input: [CapabilitySupport](api/models.md)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [CapabilitySupport](api/models.md)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [CapabilitySupport](api/models.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [ThinkingCapability](api/models.md)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](api/models.md)

Supported thinking type configurations.

adaptive: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class ModelInfo: …

id: str

Unique model identifier.

capabilities: Optional[ModelCapabilities]

Model capability information.

batch: [CapabilitySupport](api/models.md)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [CapabilitySupport](api/models.md)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [CapabilitySupport](api/models.md)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [ContextManagementCapability](api/models.md)

Context management support and available strategies.

clear\_thinking\_20251015: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[CapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [EffortCapability](api/models.md)

Effort (reasoning\_effort) support and available levels.

high: [CapabilitySupport](api/models.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [CapabilitySupport](api/models.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [CapabilitySupport](api/models.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [CapabilitySupport](api/models.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image\_input: [CapabilitySupport](api/models.md)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [CapabilitySupport](api/models.md)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [CapabilitySupport](api/models.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [ThinkingCapability](api/models.md)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](api/models.md)

Supported thinking type configurations.

adaptive: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

created\_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: str

A human-readable name for the model.

max\_input\_tokens: Optional[int]

Maximum input context window size in tokens for this model.

max\_tokens: Optional[int]

Maximum value for the `max_tokens` parameter when using this model.

type: Literal["model"]

Object type.

For Models, this is always `"model"`.

class ThinkingCapability: …

Thinking capability details.

supported: bool

Whether this capability is supported by the model.

types: [ThinkingTypes](api/models.md)

Supported thinking type configurations.

adaptive: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class ThinkingTypes: …

Supported thinking type configurations.

adaptive: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [CapabilitySupport](api/models.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
