# External Keys

Copy page



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



ExternalKeyCreateResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

created\_at: string

display\_name: string

Human-friendly display name. Null if none was set.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, type, region, role\_arn }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, type, region, role\_arn } 

kms\_arn: string

Full ARN of the AWS KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

role\_arn: optional string⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyListResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

created\_at: string

display\_name: string

Human-friendly display name. Null if none was set.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, type, region, role\_arn }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, type, region, role\_arn } 

kms\_arn: string

Full ARN of the AWS KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

role\_arn: optional string⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyRetrieveResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

created\_at: string

display\_name: string

Human-friendly display name. Null if none was set.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, type, region, role\_arn }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, type, region, role\_arn } 

kms\_arn: string

Full ARN of the AWS KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

role\_arn: optional string⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyUpdateResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

created\_at: string

display\_name: string

Human-friendly display name. Null if none was set.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, type, region, role\_arn }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, type, region, role\_arn } 

kms\_arn: string

Full ARN of the AWS KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

role\_arn: optional string⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyDeleteResponse object { id, type } 

id: string

ID of the deleted External Key.

type: "external\_key\_deleted"



ExternalKeyValidateResponse object { error, status, type } 

Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says
whether the key works.

error: string

Error message when status is `failure`. Null otherwise.



status: "failure" or "success"

`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"failure"

"success"

type: "external\_key\_validation"

---

*Copyright © Anthropic. All rights reserved.*
