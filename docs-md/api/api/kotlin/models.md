# Models

Copy page

Kotlin

# Models

##### [List Models](api/models/list.md)

models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : ModelListPage

get/v1/models

##### [Get a Model](api/models/retrieve.md)

models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [ModelInfo](api/models.md)

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class ModelInfo:

id: String

Unique model identifier.

createdAt: LocalDateTime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

displayName: String

A human-readable name for the model.

type: JsonValue; "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

MODEL("model")