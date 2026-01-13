# Models

Copy page

TypeScript

# Models

##### [List Models](api/beta/models/list.md)

client.beta.models.list(ModelListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type } >

get/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

client.beta.models.retrieve(stringmodelID, ModelRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type }

get/v1/models/{model\_id}

##### ModelsExpand Collapse

BetaModelInfo { id, created\_at, display\_name, type }

id: string

Unique model identifier.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

"model"