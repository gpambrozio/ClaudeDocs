# Models

Copy page

Python

# Models

##### [List Models](api/models/list.md)

models.list(ModelListParams\*\*kwargs)  -> SyncPage[[ModelInfo](api/models.md)]

get/v1/models

##### [Get a Model](api/models/retrieve.md)

models.retrieve(strmodel\_id, ModelRetrieveParams\*\*kwargs)  -> [ModelInfo](api/models.md)

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class ModelInfo: …

id: str

Unique model identifier.

created\_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: str

A human-readable name for the model.

type: Literal["model"]

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

"model"

---

*Copyright © Anthropic. All rights reserved.*
