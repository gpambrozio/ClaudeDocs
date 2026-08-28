# Add RBAC Group Member

Copy page



# Add RBAC Group Member

POST/v1/organizations/rbac\_groups/{group\_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

group\_id: string

ID of the RBAC Group.

##### Body

user\_id: string

ID of the User.

##### Returns



RbacGroupMember object{ created\_at, email, group\_id, 2 more }



created\_at: string

RFC 3339 timestamp of when the User was added to the RBAC Group.

formatdate-time

email: string

Email of the User.

group\_id: string

ID of the RBAC Group.



type: "rbac\_group\_member"

Object type.

For RBAC Group Members, this is always `"rbac_group_member"`.

defaultrbac\_group\_member

user\_id: string

ID of the User.



### Add RBAC Group Member

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/rbac_groups/$GROUP_ID/members \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        }'
```

Response 200



```shiki
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

##### Returns Examples

Response 200



```shiki
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

---

*Copyright © Anthropic. All rights reserved.*
