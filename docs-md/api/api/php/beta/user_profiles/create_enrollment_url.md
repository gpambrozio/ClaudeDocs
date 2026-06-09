# Create Enrollment URL

Copy page

SDK language

PHP

# Create Enrollment URL

$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfileEnrollmentURL](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

Create Enrollment URL

##### ParametersExpand Collapse

userProfileID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[BetaUserProfileEnrollmentURL](api/beta.md)

\Datetime expiresAt

A timestamp in RFC 3339 format

Type type

Object type. Always `enrollment_url`.

string url

Enrollment URL to send to the end user. Valid until `expires_at`.

Create Enrollment URL

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfileEnrollmentURL = $client
  ->beta
  ->userProfiles
  ->createEnrollmentURL(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9', betas: ['message-batches-2024-09-24']
);

var_dump($betaUserProfileEnrollmentURL);
```

Response 200



```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

##### Returns Examples

Response 200



```shiki
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

---

*Copyright © Anthropic. All rights reserved.*
