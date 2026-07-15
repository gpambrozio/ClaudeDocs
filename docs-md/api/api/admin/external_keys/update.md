# Update External Key

Copy page



# Update External Key

POST/v1/organizations/external\_keys/{external\_key\_id}

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

##### Path ParametersExpand Collapse

external\_key\_id: string

ID of the External Key.

##### Body ParametersJSONExpand Collapse

display\_name: optional string

Human-friendly display name.

geo: optional "us"

Data residency geo. Only `us` is supported.



provider\_config: optional object { kms\_arn, type, region, role\_arn }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, type, region, role\_arn } 

kms\_arn: string

Full ARN of the AWS KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.

Deprecatedrole\_arn: optional string

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

Azure Key Vault provider configuration.

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — https://<vault-name>.vault.azure.net or https://<hsm-name>.managedhsm.azure.net.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

##### ReturnsExpand Collapse

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

Deprecatedrole\_arn: optional string

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

Update External Key



```shiki
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

Response 200



```shiki
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
