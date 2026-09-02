# Remove RBAC Group Member

Copy page



# Remove RBAC Group Member

DELETE/v1/organizations/rbac\_groups/{group\_id}/members/{user\_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

group\_id: string

ID of the RBAC Group.

user\_id: string

ID of the User.

##### Returns



RbacGroupMemberDeleted object{ group\_id, type, user\_id }

group\_id: string

ID of the RBAC Group.



type: "rbac\_group\_member\_deleted"

Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

defaultrbac\_group\_member\_deleted

user\_id: string

ID of the User.

Remove RBAC Group Member

cURL

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
