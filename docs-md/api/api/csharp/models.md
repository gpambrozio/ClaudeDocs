# Models

Copy page

C#

# Models

##### [List Models](api/models/list.md)

[ModelListPageResponse](api/models.md) Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/models/retrieve.md)

[ModelInfo](api/models.md) Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class ModelInfo:

required string ID

Unique model identifier.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.

---

*Copyright © Anthropic. All rights reserved.*
