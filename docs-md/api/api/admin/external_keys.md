# External Keys

Copy page



# External Keys

##### [Create External Key](api/http/admin/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/http/admin/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/http/admin/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/http/admin/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/http/admin/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/http/admin/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

##### Models



ExternalKeyCreateResponse object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).



ExternalKeyRetrieveResponse object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).



ExternalKeyUpdateResponse object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).



ExternalKeyListResponse object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).



ExternalKeyDeleteResponse object{ id, type }

id: string

ID of the deleted External Key.



type: "external\_key\_deleted"

defaultexternal\_key\_deleted



ExternalKeyValidateResponse object{ error, status, type }

Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says
whether the key works.

error: string or null

Error message when status is `failure`. Null otherwise.



status: "failure" or "success"

`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"failure"

"success"



type: "external\_key\_validation"

defaultexternal\_key\_validation

---

*Copyright © Anthropic. All rights reserved.*
