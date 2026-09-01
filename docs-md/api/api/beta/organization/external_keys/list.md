# List External Keys

Copy page



cURL

# List External Keys

GET/v1/organizations/external\_keys

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

##### Query parameters



limit: optional number

Number of results per page.

default20

maximum100

minimum1

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [BetaExternalKey](api/http/beta/organization/external_keys.md) { id, attachment, created\_at, 5 more }

id: string

Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.



attachment: [BetaExternalKeyAttachedAttachment](api/http/beta/organization/external_keys.md) { type } or [BetaExternalKeyUnattachedAttachment](api/http/beta/organization/external_keys.md) { type }

Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

One of the following:



BetaExternalKeyAttachedAttachment object{ type }



type: "attached"

defaultattached



BetaExternalKeyUnattachedAttachment object{ type }



type: "unattached"

defaultunattached



created\_at: string

formatdate-time

display\_name: string or null

Human-friendly display name. Null if none was set.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: [BetaAWSExternalKeyConfig](api/http/beta/organization/external_keys.md) { kms\_arn, type, region, role\_arn } or [BetaGCPExternalKeyConfig](api/http/beta/organization/external_keys.md) { key\_name, type } or [BetaAzureExternalKeyConfig](api/http/beta/organization/external_keys.md) { key\_name, tenant\_id, type, 2 more }

KMS provider identity and auth coordinates.

One of the following:



BetaAWSExternalKeyConfig object{ kms\_arn, type, region, role\_arn }



kms\_arn: string

Full ARN of the AWS KMS key.

maxLength2048

type: "aws"

region: optional string or null

AWS region. Derived from `kms_arn` if omitted.

role\_arn: optional string or null⁠Deprecated

IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.



BetaGCPExternalKeyConfig object{ key\_name, type }

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



BetaAzureExternalKeyConfig object{ key\_name, tenant\_id, type, 2 more }

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client\_id: optional string or null

Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.



type: "external\_key"

defaultexternal\_key



updated\_at: string

formatdate-time

next\_page: string or null

Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

List External Keys

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
