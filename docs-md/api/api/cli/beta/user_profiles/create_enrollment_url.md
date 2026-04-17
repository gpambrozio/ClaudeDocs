# Create Enrollment URL

Copy page

CLI

# Create Enrollment URL

$ ant beta:user-profiles create-enrollment-url

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

Create Enrollment URL

##### ParametersExpand Collapse

--user-profile-id: string

Path parameter user\_profile\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_user\_profile\_enrollment\_url: object { expires\_at, type, url }

expires\_at: string

A timestamp in RFC 3339 format

type: "enrollment\_url"

Object type. Always `enrollment_url`.

"enrollment\_url"

url: string

Enrollment URL to send to the end user. Valid until `expires_at`.

Create Enrollment URL

CLI

```shiki
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
```

Response 200

```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

##### Returns Examples

Response 200

```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

---

*Copyright © Anthropic. All rights reserved.*
