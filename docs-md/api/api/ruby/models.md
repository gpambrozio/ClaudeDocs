# Models

Copy page

Ruby

# Models

##### [List Models](api/models/list.md)

models.list(\*\*kwargs) -> Page<[ModelInfo](api/models.md) { id, created\_at, display\_name, type } >

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

models.retrieve(model\_id, \*\*kwargs) -> [ModelInfo](api/models.md) { id, created\_at, display\_name, type }

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class ModelInfo { id, created\_at, display\_name, type }

id: String

Unique model identifier.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: String

A human-readable name for the model.

type: :model

Object type.

For Models, this is always `"model"`.

---

*Copyright © Anthropic. All rights reserved.*
