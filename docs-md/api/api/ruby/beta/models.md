# Models

Copy page

Ruby

# Models

##### [List Models](api/beta/models/list.md)

beta.models.list(\*\*kwargs) -> Page<[BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type } >

get/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type }

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaModelInfo { id, created\_at, display\_name, type }

id: String

Unique model identifier.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: String

A human-readable name for the model.

type: :model

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

:model