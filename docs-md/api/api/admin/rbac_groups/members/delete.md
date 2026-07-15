# Remove RBAC Group Member

Copy page



# Remove RBAC Group Member

DELETE/v1/organizations/rbac\_groups/{group\_id}/members/{user\_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is in beta and available to Claude Enterprise organizations only. Requests must send the `ce-user-management-2026-07-13` value in the `anthropic-beta` header.

##### Path ParametersExpand Collapse

group\_id: string

ID of the RBAC Group.

user\_id: string

ID of the User.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



RbacGroupMemberDeleted object { group\_id, type, user\_id } 

group\_id: string

ID of the RBAC Group.

type: "rbac\_group\_member\_deleted"

Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

user\_id: string

ID of the User.

Remove RBAC Group Member



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

##### Returns Examples

Response 200



```shiki
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

---

*Copyright © Anthropic. All rights reserved.*
