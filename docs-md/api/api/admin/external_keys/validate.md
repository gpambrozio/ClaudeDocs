# Validate External Key

Copy page

# Validate External Key

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

##### Path ParametersExpand Collapse

external\_key\_id: string

ID of the External Key to validate.

##### ReturnsExpand Collapse

error: string

Error message when status is `failure`. Null otherwise.



status: "success" or "failure"

`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"success"

"failure"

type: "external\_key\_validation"

Validate External Key



```shiki
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "error": null,
  "status": "success",
  "type": "external_key_validation"
}
```

##### Returns Examples

Response 200



```shiki
{
  "error": null,
  "status": "success",
  "type": "external_key_validation"
}
```

---

*Copyright © Anthropic. All rights reserved.*
