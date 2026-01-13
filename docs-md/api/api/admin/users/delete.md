# Remove User

Copy page

# Remove User

delete/v1/organizations/users/{user\_id}

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

Accepts one of the following:

"user\_deleted"

Remove User

```shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```