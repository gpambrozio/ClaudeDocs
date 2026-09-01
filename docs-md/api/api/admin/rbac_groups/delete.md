# Delete RBAC Group

Copy page



# Delete RBAC Group

DELETE/v1/organizations/rbac\_groups/{group\_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API.

The RBAC Groups API is available to Claude Enterprise organizations only.

##### Path parameters

group\_id: string

ID of the RBAC Group.

##### Returns



RbacGroupDeleted object{ id, type }

id: string

ID of the RBAC Group.



type: "rbac\_group\_deleted"

Deleted object type.

For RBAC Groups, this is always `"rbac_group_deleted"`.

defaultrbac\_group\_deleted

Delete RBAC Group

cURL

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
