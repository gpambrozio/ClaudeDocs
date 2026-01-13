# Users

Copy page

# Users

##### [Get User](api/admin/users/retrieve.md)

get/v1/organizations/users/{user\_id}

##### [List Users](api/admin/users/list.md)

get/v1/organizations/users

##### [Update User](api/admin/users/update.md)

post/v1/organizations/users/{user\_id}

##### [Remove User](api/admin/users/delete.md)

delete/v1/organizations/users/{user\_id}

##### ModelsExpand Collapse

User = object { id, added\_at, email, 3 more }

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

formatdate-time

email: string

Email of the User.

name: string

Name of the User.

role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

type: "user"

Object type.

For Users, this is always `"user"`.

Accepts one of the following:

"user"