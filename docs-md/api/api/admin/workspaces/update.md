# Update Workspace

Copy page



# Update Workspace

POST/v1/organizations/workspaces/{workspace\_id}

Update Workspace

##### Path parameters

workspace\_id: string

##### Body



data\_residency: optional object{ allowed\_inference\_geos, default\_inference\_geo } or null

Data residency configuration for the workspace.



allowed\_inference\_geos: optional array of "global" or "us" or "unrestricted" or null

Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



array of "global" or "us"

One of the following:

"global"

"us"

"unrestricted"



default\_inference\_geo: optional "global" or "us" or null

Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"

"us"



display\_color: optional string

Hex color code representing the Workspace in the Anthropic Console.

maxLength7

pattern^#[0-9A-Fa-f]{6}$

external\_key\_id: optional string

ID of the customer-managed encryption key (CMEK) configuration to use for this
Workspace. Setting this field requires CMEK to be enabled for your
organization. When set, data stored for this Workspace is encrypted with the
referenced key. Create key configurations with the External Keys API. On
Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
single-Region key in the same AWS account and Region as the Workspace. On that
platform the key is validated against this Workspace when it is attached, so a
key-policy problem is reported as an error on this request. This field is write-once:
once a key is attached to a Workspace it cannot be detached or replaced. To
rotate key material, rotate the underlying key on your cloud KMS; the
`external_key_id` stays the same.



name: optional string

Name of the Workspace.

maxLength40

minLength1

tags: optional map[string] or null

User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

##### Returns



Workspace object{ id, archived\_at, compartment\_id, 7 more }

Update Workspace

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          }
        }'
```

Response 200



```shiki
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

---

*Copyright © Anthropic. All rights reserved.*
