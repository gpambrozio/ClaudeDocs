# Delete Skill Version

Copy page

PHP

# Delete Skill Version

$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): [VersionDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

Delete Skill Version

##### ParametersExpand Collapse

skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.

version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[VersionDeleteResponse](api/beta.md)

string id

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

string type

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

Delete Skill Version

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->delete(
  'version', skillID: 'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($version);
```

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

---

*Copyright © Anthropic. All rights reserved.*
