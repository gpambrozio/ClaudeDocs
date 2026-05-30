# Delete Environment

Copy page

SDK language

PHP

# Delete Environment

$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas): [BetaEnvironmentDeleteResponse](api/beta.md)

DELETE/v1/environments/{environment\_id}

Delete an environment by ID. Returns a confirmation of the deletion.

##### ParametersExpand Collapse

environmentID: string

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[BetaEnvironmentDeleteResponse](api/beta.md)

string id

Environment identifier

"environment\_deleted" type

The type of response

Delete Environment

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironmentDeleteResponse = $client->beta->environments->delete(
  'env_011CZkZ9X2dpNyB7HsEFoRfW', betas: ['message-batches-2024-09-24']
);

var_dump($betaEnvironmentDeleteResponse);
```

Response 200

```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
