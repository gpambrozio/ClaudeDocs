# Delete RBAC Group

Copy page



# Delete RBAC Group

DELETE/v1/organizations/rbac\_groups/{group\_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Path ParametersExpand Collapse

group\_id: string

ID of the RBAC Group.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



RbacGroupDeleted object { id, type } 

id: string

ID of the RBAC Group.



type: "rbac\_group\_deleted"

Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

Delete RBAC Group



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
