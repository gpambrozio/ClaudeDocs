# Create Invite

Copy page

# Create Invite

POST/v1/organizations/invites

Create Invite

##### Body ParametersJSONExpand Collapse

email: string

Email of the User.

role: "user" or "developer" or "billing" or 2 more

Role for the invited User. Cannot be "admin".

Accepts one of the following:

"user"

"developer"

"billing"

"claude\_code\_user"

"managed"

##### ReturnsExpand Collapse

Invite = object { id, email, expires\_at, 4 more }

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.

role: "user" or "developer" or "billing" or 3 more

Organization role of the User.

Accepts one of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"

"managed"

status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

Accepts one of the following:

"accepted"

"expired"

"deleted"

"pending"

type: "invite"

Object type.

For Invites, this is always `"invite"`.

Create Invite

```shiki
curl https://api.anthropic.com/v1/organizations/invites \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
    -d '{
          "email": "user@emaildomain.com",
          "role": "user"
        }'
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
