# Delete Spend Limit

Copy page



# Delete Spend Limit

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

Delete a per-user spend limit override.

The member falls back to any inherited spend limit at that period.
Seat-tier, group, and organization-level rows cannot be deleted via
this endpoint.

##### Path ParametersExpand Collapse

spend\_limit\_id: string

ID of the Spend Limit.

##### ReturnsExpand Collapse

id: string

type: "spend\_limit\_deleted"

Delete Spend Limit



```shiki
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
