# Get Current Organization

Copy page



cURL

# Get Current Organization

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### Returns



BetaOrganization object{ id, name, type }



id: string

ID of the Organization.

formatuuid

name: string

Name of the Organization.



type: "organization"

Object type.

For Organizations, this is always `"organization"`.

defaultorganization



### Get Current Organization

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/me \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

---

*Copyright © Anthropic. All rights reserved.*
