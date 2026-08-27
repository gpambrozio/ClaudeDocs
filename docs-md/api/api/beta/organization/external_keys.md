# External Keys

Copy page



cURL

# External Keys

##### [Create External Key](api/http/beta/organization/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/http/beta/organization/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/http/beta/organization/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/http/beta/organization/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/http/beta/organization/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/http/beta/organization/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

##### Models



BetaAWSExternalKeyConfig object{ kms\_arn, type, region, role\_arn }



kms\_arn: string

Full ARN of the AWS KMS key.

maxLength2048

type: "aws"

region: optional string or null

AWS region. Derived from `kms_arn` if omitted.

role\_arn: optional string or null⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



BetaAzureExternalKeyConfig object{ key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client\_id: optional string or null

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.



BetaAzureExternalKeyConfigParam object{ key\_name, tenant\_id, type, 2 more }

Azure Key Vault provider configuration.

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client\_id: optional string or null

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.



BetaExternalKey object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).



BetaExternalKeyAttachedAttachment object{ type }



type: "attached"

defaultattached



BetaExternalKeyUnattachedAttachment object{ type }



type: "unattached"

defaultunattached



BetaGCPExternalKeyConfig object{ key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"

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
