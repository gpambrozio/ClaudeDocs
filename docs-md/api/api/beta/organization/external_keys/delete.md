# Delete External Key

Copy page



cURL

# Delete External Key

DELETE/v1/organizations/external\_keys/{external\_key\_id}

Delete an external key config.

The request is rejected if any workspace still references this config.

##### Path parameters



external\_key\_id: string

ID of the External Key.

maxLength2048

##### Returns

id: string

ID of the deleted External Key.



type: "external\_key\_deleted"

defaultexternal\_key\_deleted

### Delete External Key

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
