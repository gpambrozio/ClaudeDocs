# List RBAC Role Permissions

Copy page



# List RBAC Role Permissions

GET/v1/organizations/rbac\_roles/{role\_id}/permissions

List the permissions an RBAC Role grants.

The RBAC Roles API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Path ParametersExpand Collapse

role\_id: string

ID of the RBAC Role.

##### Query ParametersExpand Collapse



limit: optional number

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

maximum1000

minimum1

page: optional string

Optionally set to the `next_page` token from the previous response.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



data: array of [RbacRolePermission](api/admin/rbac_roles/permissions.md) { action, resource, type } 



action: string

Action the permission grants on the resource.

The vocabulary follows the resource: an `organization` grant carries a
product-feature entitlement (for example `chat`), an admin-panel
permission entitlement (`permission_*`), or a blanket capability-access
mode — `capability_access_all` grants every product-feature entitlement,
and `capability_access_all_ga` grants the generally-available subset as
it stands at permission-check time; neither mode grants model-access
entitlements. A consumer enumerating a role's per-feature grants should
treat a blanket row as granting every product-feature entitlement it
covers, or it will under-report the role's effective access. A `connector_tool` grant carries
a tool-access action (`use` or `always_allow`); a `connector_scope` grant
carries the scope action `grant` (the role may receive the named OAuth
scope when tokens are minted for the connector); `connector` and
`all_connectors` grants carry a tool-access action, the scope action, or
an authentication-method action (`interactive` or `managed`).



resource: object { organization\_id, type }  or object { connector\_id, tool\_name, type }  or object { connector\_id, scope, type }  or 2 more

What the permission applies to.

A tagged union: `type` names the kind of resource and determines which
identifier fields are present.

One of the following:



Organization object { organization\_id, type } 

organization\_id: string

UUID of the organization the permission applies to.

type: "organization"

Kind of resource the permission applies to.



ConnectorTool object { connector\_id, tool\_name, type } 

connector\_id: string

ID of the connector the permission applies to.



tool\_name: string

Published name of the connector tool the permission applies to.

When the published name contains characters outside `[a-zA-Z0-9_-]` (or
collides with a reserved form), it is server-encoded into a stable
`{prefix}_{32-hex}` form — a shortened readable prefix of the name plus
a hash — from which the published name is not recoverable.

type: "connector\_tool"

Kind of resource the permission applies to.



ConnectorScope object { connector\_id, scope, type } 

connector\_id: string

ID of the connector the permission applies to.



scope: string

OAuth scope the permission names — the role may receive this scope when
tokens are minted for the connector.

Subject to the same encoding rule as `tool_name`: a scope containing
characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form)
appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth
scopes routinely contain `:` and `/`, so most appear encoded.

type: "connector\_scope"

Kind of resource the permission applies to.



Connector object { connector\_id, type } 

connector\_id: string

ID of the connector the permission applies to.

type: "connector"

Kind of resource the permission applies to.



AllConnectors object { type } 

type: "all\_connectors"

Kind of resource the permission applies to.



type: "rbac\_role\_permission"

Object type.

For RBAC Role Permissions, this is always `"rbac_role_permission"`.

has\_more: boolean

Indicates whether there are more results beyond this page.

next\_page: string

Opaque cursor for the next page. Pass as the `page` parameter on the next
request.

List RBAC Role Permissions



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

---

*Copyright © Anthropic. All rights reserved.*
