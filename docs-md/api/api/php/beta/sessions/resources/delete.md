# Delete Session Resource

Copy page

PHP

# Delete Session Resource

$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): [ManagedAgentsDeleteSessionResource](api/beta.md)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

Delete Session Resource

##### ParametersExpand Collapse

sessionID: string

resourceID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[ManagedAgentsDeleteSessionResource](api/beta.md)

string id

Type type

Delete Session Resource

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeleteSessionResource = $client
  ->beta
  ->sessions
  ->resources
  ->delete(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsDeleteSessionResource);
```

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
