# Remove User

Copy page

# Remove User

DELETE/v1/organizations/users/{user\_id}

Remove User

##### Path ParametersExpand Collapse

user\_id: string

ID of the User.

##### ReturnsExpand Collapse

id: string

ID of the User.

type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

Remove User

```shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
