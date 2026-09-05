# Update User

Copy page



# Update User

POST/v1/organizations/users/{user\_id}

Update a member's organization role.

##### Path parameters

user\_id: string

ID of the User.

##### Body



role: "billing" or "claude\_code\_user" or "developer" or 2 more

New role for the User.

The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

One of the following:

"billing"

"claude\_code\_user"

"developer"

"managed"

"user"

##### Returns



User object{ id, added\_at, email, 3 more }

id: string

ID of the User.



added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

formatdate-time

email: string

Email of the User.

name: string

Name of the User.



role: "admin" or "billing" or "claude\_code\_user" or 6 more

Organization role of the User.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"



type: "user"

Object type.

For Users, this is always `"user"`.

defaultuser

Update User

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
    -d '{
          "role": "user"
        }'
```

Response 200



```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "user",
  "type": "user"
}
```

---

*Copyright © Anthropic. All rights reserved.*
