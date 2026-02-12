# Models

Copy page

Java

# Models

##### [List Models](api/beta/models/list.md)

ModelListPage beta().models().list(ModelListParamsparams = ModelListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta.md) beta().models().retrieve(ModelRetrieveParamsparams = ModelRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaModelInfo:

String id

Unique model identifier.

LocalDateTime createdAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

String displayName

A human-readable name for the model.

JsonValue; type "model"constant"model"constant

Object type.

For Models, this is always `"model"`.

---

*Copyright © Anthropic. All rights reserved.*
