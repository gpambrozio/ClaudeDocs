# Models

Copy page

Java

# Models

##### [List Models](api/models/list.md)

ModelListPage models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/models

##### [Get a Model](api/models/retrieve.md)

[ModelInfo](api/models.md) models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class ModelInfo:

String id

Unique model identifier.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

String displayName

A human-readable name for the model.

JsonValue; type "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

MODEL("model")

---

*Copyright © Anthropic. All rights reserved.*
