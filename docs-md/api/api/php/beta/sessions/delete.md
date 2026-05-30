# Delete Session

Copy page

SDK language

PHP

# Delete Session

$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedSession](api/beta.md)

DELETE/v1/sessions/{session\_id}

Delete Session

##### ParametersExpand Collapse

sessionID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[BetaManagedAgentsDeletedSession](api/beta.md)

string id

Type type

Delete Session

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedSession = $client->beta->sessions->delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7', betas: ['message-batches-2024-09-24']
);

var_dump($betaManagedAgentsDeletedSession);
```

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
