# External Keys

Copy page

# External Keys

##### [Create External Key](api/admin/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/admin/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/admin/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/admin/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/admin/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/admin/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

##### ModelsExpand Collapse

ExternalKeyCreateResponse object { id, created\_at, display\_name, 4 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more }

KMS provider identity and auth coordinates.

One of the following:

Aws object { kms\_arn, role\_arn, type, region }

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

Gcp object { key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"

Azure object { key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string

ExternalKeyListResponse object { data, next\_page }

Opaque-cursor page of external keys, ordered by creation time (newest first).

data: array of object { id, created\_at, display\_name, 4 more }

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more }

KMS provider identity and auth coordinates.

One of the following:

Aws object { kms\_arn, role\_arn, type, region }

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

Gcp object { key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"

Azure object { key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string

next\_page: string

Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

ExternalKeyRetrieveResponse object { id, created\_at, display\_name, 4 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more }

KMS provider identity and auth coordinates.

One of the following:

Aws object { kms\_arn, role\_arn, type, region }

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

Gcp object { key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"

Azure object { key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string

ExternalKeyUpdateResponse object { id, created\_at, display\_name, 4 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more }

KMS provider identity and auth coordinates.

One of the following:

Aws object { kms\_arn, role\_arn, type, region }

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

Gcp object { key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"

Azure object { key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string

ExternalKeyDeleteResponse object { id, type }

id: string

ID of the deleted External Key.

type: "external\_key\_deleted"

ExternalKeyValidateResponse object { error, status, type }

Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says
whether the key works.

error: string

Error message when status is `failure`. Null otherwise.

status: "success" or "failure"

`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"success"

"failure"

type: "external\_key\_validation"

---

*Copyright © Anthropic. All rights reserved.*
