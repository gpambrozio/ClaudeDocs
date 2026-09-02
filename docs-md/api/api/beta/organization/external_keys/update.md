# Update External Key

Copy page



cURL

# Update External Key

POST/v1/organizations/external\_keys/{external\_key\_id}

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

##### Path parameters



external\_key\_id: string

ID of the External Key.

maxLength2048

##### Body



display\_name: optional string or null

Human-friendly display name.

maxLength255

minLength1

geo: optional "us" or null

Data residency geo. Only `us` is supported.



provider\_config: optional [BetaAWSExternalKeyConfig](api/http/beta/organization/external_keys.md) { kms\_arn, type, region, role\_arn } or [BetaGCPExternalKeyConfig](api/http/beta/organization/external_keys.md) { key\_name, type } or [BetaAzureExternalKeyConfigParam](api/http/beta/organization/external_keys.md) { key\_name, tenant\_id, type, 2 more } or null

KMS provider identity and auth coordinates.

One of the following:



BetaAWSExternalKeyConfig object{ kms\_arn, type, region, role\_arn }



kms\_arn: string

Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

maxLength2048

type: "aws"

region: optional string or null

AWS region. Derived from `kms_arn` if omitted.

role\_arn: optional string or null⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.



BetaGCPExternalKeyConfig object{ key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



BetaAzureExternalKeyConfigParam object{ key\_name, tenant\_id, type, 2 more }

Azure Key Vault provider configuration.

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client\_id: optional string or null

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

##### Returns



BetaExternalKey object{ id, attachment, created\_at, 5 more }

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

Update External Key

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```shiki
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
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
  "attachment": {
    "type": "attached"
  },
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
