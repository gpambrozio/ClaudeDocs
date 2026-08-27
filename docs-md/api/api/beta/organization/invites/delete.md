# Delete Invite

Copy page



cURL

# Delete Invite

DELETE/v1/organizations/invites/{invite\_id}

Delete a pending invite.

##### Path parameters

invite\_id: string

ID of the Invite.

##### Returns

id: string

ID of the Invite.



type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

defaultinvite\_deleted

### Delete Invite

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/invites/$INVITE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
