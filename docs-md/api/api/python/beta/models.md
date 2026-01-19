# Models

Copy page

Python

# Models

##### [List Models](api/beta/models/list.md)

beta.models.list(ModelListParams\*\*kwargs)  -> SyncPage[[BetaModelInfo](api/beta.md)]

get/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(strmodel\_id, ModelRetrieveParams\*\*kwargs)  -> [BetaModelInfo](api/beta.md)

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaModelInfo: …

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
