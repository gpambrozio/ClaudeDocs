# Get Current Organization

Copy page

# Get Current Organization

get/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### ReturnsExpand Collapse

Organization = object { id, name, type }

id: string

ID of the Organization.

formatuuid

name: string

Name of the Organization.

type: "organization"

Object type.

For Organizations, this is always `"organization"`.

Accepts one of the following:

"organization"

Get Current Organization

```shiki
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200

```shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

---

*Copyright © Anthropic. All rights reserved.*
