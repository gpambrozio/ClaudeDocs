# Delete Invite

Copy page

# Delete Invite

DELETE/v1/organizations/invites/{invite\_id}

Delete Invite

##### Path ParametersExpand Collapse

invite\_id: string

ID of the Invite.

##### ReturnsExpand Collapse

id: string

ID of the Invite.

type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

Delete Invite

```shiki
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
