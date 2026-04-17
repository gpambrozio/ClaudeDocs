# Models

Copy page

Python

# Models

##### [List Models](api/beta/models/list.md)

beta.models.list(ModelListParams\*\*kwargs)  -> SyncPage[[BetaModelInfo](api/beta.md)]

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(strmodel\_id, ModelRetrieveParams\*\*kwargs)  -> [BetaModelInfo](api/beta.md)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaCapabilitySupport: …

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class BetaContextManagementCapability: …

Context management capability details.

clear\_thinking\_20251015: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class BetaEffortCapability: …

Effort (reasoning\_effort) capability details.

high: [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

xhigh: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class BetaModelCapabilities: …

Model capability information.

batch: [BetaCapabilitySupport](api/beta.md)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](api/beta.md)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [BetaCapabilitySupport](api/beta.md)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [BetaContextManagementCapability](api/beta.md)

Context management support and available strategies.

clear\_thinking\_20251015: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](api/beta.md)

Effort (reasoning\_effort) support and available levels.

high: [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

xhigh: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

image\_input: [BetaCapabilitySupport](api/beta.md)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [BetaCapabilitySupport](api/beta.md)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [BetaCapabilitySupport](api/beta.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](api/beta.md)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaModelInfo: …

id: str

Unique model identifier.

capabilities: Optional[BetaModelCapabilities]

Model capability information.

batch: [BetaCapabilitySupport](api/beta.md)

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](api/beta.md)

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [BetaCapabilitySupport](api/beta.md)

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [BetaContextManagementCapability](api/beta.md)

Context management support and available strategies.

clear\_thinking\_20251015: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](api/beta.md)

Effort (reasoning\_effort) support and available levels.

high: [BetaCapabilitySupport](api/beta.md)

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md)

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md)

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md)

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

xhigh: Optional[BetaCapabilitySupport]

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

image\_input: [BetaCapabilitySupport](api/beta.md)

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [BetaCapabilitySupport](api/beta.md)

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [BetaCapabilitySupport](api/beta.md)

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](api/beta.md)

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md)

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

class BetaThinkingCapability: …

Thinking capability details.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md)

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaThinkingTypes: …

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md)

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

---

*Copyright © Anthropic. All rights reserved.*
