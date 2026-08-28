# Users

Copy page



cURL

# Users

##### [List Users](api/http/beta/organization/users/list.md)

GET/v1/organizations/users

##### [Get User](api/http/beta/organization/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [Update User](api/http/beta/organization/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/http/beta/organization/users/remove.md)

DELETE/v1/organizations/users/{user\_id}

##### Models



BetaOrganizationUser object{ id, added\_at, email, 3 more }

id: string

ID of the User.



added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

formatdate-time

email: string

Email of the User.

name: string

Name of the User.



role: [BetaOrganizationRole](api/http/beta/organization.md)

Organization role of the User.

One of the following:

"admin"

"billing"

"claude\_code\_user"

"developer"

"managed"

"membership\_admin"

"owner"

"primary\_owner"

"user"



type: "user"

Object type.

For Users, this is always `"user"`.

defaultuser



UserRemoveResponse object{ id, type }

id: string

ID of the User.



type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

defaultuser\_deleted

---

*Copyright © Anthropic. All rights reserved.*
