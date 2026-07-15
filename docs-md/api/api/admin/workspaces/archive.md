# Archive Workspace

Copy page



# Archive Workspace

POST/v1/organizations/workspaces/{workspace\_id}/archive

Archive Workspace

##### Path ParametersExpand Collapse

workspace\_id: string

##### ReturnsExpand Collapse



Workspace object { id, archived\_at, compartment\_id, 7 more } 

id: string

ID of the Workspace.

archived\_at: string

RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

compartment\_id: string

Identifier for this Workspace's encryption compartment. When you configure a
customer-managed encryption key (CMEK) on AWS, reference this value in your
KMS key-policy condition so the key is scoped to this compartment. On GCP and
Azure, Anthropic enforces the compartment binding automatically; you do not
need to reference this value in your key configuration. See the CMEK integration guide for the
required key configuration, including the value used during key validation.

created\_at: string

RFC 3339 datetime string indicating when the Workspace was created.



data\_residency: object { allowed\_inference\_geos, default\_inference\_geo, workspace\_geo } 

Data residency configuration.



allowed\_inference\_geos: array of string or "unrestricted"

Permitted inference geo values. 'unrestricted' means all geos are allowed.

One of the following:

array of string

"unrestricted"

default\_inference\_geo: string

Default inference geo applied when requests omit the parameter.

workspace\_geo: string

Geographic region for workspace data storage. Immutable after creation.

display\_color: string

Hex color code representing the Workspace in the Anthropic Console.

external\_key\_id: string

ID of the customer-managed encryption key (CMEK) configuration to use for this
Workspace. Setting this field requires CMEK to be enabled for your
organization. When set, data stored for this Workspace is encrypted with the
referenced key. Create key configurations with the External Keys API. This
field is write-once: once a key is attached to a Workspace it cannot be
detached or replaced. To rotate key material, rotate the underlying key on
your cloud KMS; the `external_key_id` stays the same.

name: string

Name of the Workspace.

tags: map[string]

User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.



type: "workspace"

Object type.

For Workspaces, this is always `"workspace"`.

Archive Workspace



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
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
