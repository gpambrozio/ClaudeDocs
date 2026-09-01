# Users

Copy page



# Users

##### [Get User](api/http/admin/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [List Users](api/http/admin/users/list.md)

GET/v1/organizations/users

##### [Update User](api/http/admin/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/http/admin/users/delete.md)

DELETE/v1/organizations/users/{user\_id}

##### Models

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



UserDeleteResponse object{ id, type }

id: string

ID of the User.



type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

defaultuser\_deleted

---

*Copyright © Anthropic. All rights reserved.*
