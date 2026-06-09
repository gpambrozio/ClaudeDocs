# Create External Key

Copy page

# Create External Key

POST/v1/organizations/external\_keys

Create an external key config owned by the caller's organization.

##### Body ParametersJSONExpand Collapse

display\_name: string

Human-friendly display name.

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

geo: optional "us"

Data residency geo. Only `us` is supported.

##### ReturnsExpand Collapse

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

Create External Key



```shiki
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "display_name": "x",
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
            "type": "aws"
          }
        }'
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
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
    "type": "aws",
    "region": "us-east-1"
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
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
    "type": "aws",
    "region": "us-east-1"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
