# Update User

Copy page

# Update User

POST/v1/organizations/users/{user\_id}

Update User

##### Path ParametersExpand Collapse

user\_id: string

ID of the User.

##### Body ParametersJSONExpand Collapse

role: "user" or "developer" or "billing" or 2 more

New role for the User. Cannot be "admin".

Accepts one of the following:

"user"

"developer"

"billing"

"claude\_code\_user"

"managed"

##### ReturnsExpand Collapse

User = object { id, added\_at, email, 3 more }

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 3 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

"managed"

type: "user"

Object type.

For Users, this is always `"user"`.

Update User

```shiki
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "role": "user"
        }'
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
