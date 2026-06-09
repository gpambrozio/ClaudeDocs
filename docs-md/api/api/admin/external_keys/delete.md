# Delete External Key

Copy page

# Delete External Key

DELETE/v1/organizations/external\_keys/{external\_key\_id}

Delete an external key config.

The request is rejected if any workspace still references this config.

##### Path ParametersExpand Collapse

external\_key\_id: string

ID of the External Key to delete.

##### ReturnsExpand Collapse

id: string

ID of the deleted External Key.

type: "external\_key\_deleted"

Delete External Key



```shiki
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200



```shiki
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
