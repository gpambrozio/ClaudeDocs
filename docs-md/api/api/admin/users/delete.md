# Remove User

Copy page



# Remove User

DELETE/v1/organizations/users/{user\_id}

Remove a member from the organization.

##### Path parameters

user\_id: string

ID of the User.

##### Returns

id: string

ID of the User.



type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

defaultuser\_deleted



### Remove User

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
