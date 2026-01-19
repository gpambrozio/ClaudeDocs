# Models

Copy page

Go

# Models

##### [List Models](api/models/list.md)

client.Models.List(ctx, params) (\*Page[[ModelInfo](api/models.md)], error)

get/v1/models

##### [Get a Model](api/models/retrieve.md)

client.Models.Get(ctx, modelID, query) (\*[ModelInfo](api/models.md), error)

get/v1/models/{model\_id}

##### ModelsExpand Collapse

type ModelInfo struct{…}

ID string

Unique model identifier.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

DisplayName string

A human-readable name for the model.

Type Model

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

const ModelModel Model = "model"

---

*Copyright © Anthropic. All rights reserved.*
