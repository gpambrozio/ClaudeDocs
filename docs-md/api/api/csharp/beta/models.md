# Models

Copy page

C#

# Models

##### [List Models](api/beta/models/list.md)

[ModelListPageResponse](api/beta.md) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

[BetaModelInfo](api/beta.md) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaModelInfo:

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
