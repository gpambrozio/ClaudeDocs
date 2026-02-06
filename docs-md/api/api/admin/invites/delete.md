# Delete Invite

Copy page

# Delete Invite

delete/v1/organizations/invites/{invite\_id}

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

Accepts one of the following:

"invite\_deleted"

Delete Invite

```shiki
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
