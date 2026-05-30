# Delete Skill

Copy page

SDK language

PHP

# Delete Skill

$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): [SkillDeleteResponse](api/beta.md)

DELETE/v1/skills/{skill\_id}

Delete Skill

##### ParametersExpand Collapse

skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[SkillDeleteResponse](api/beta.md)

string id

Unique identifier for the skill.

The format and length of IDs may change over time.

string type

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->delete(
  'skill_id', betas: ['message-batches-2024-09-24']
);

var_dump($skill);
```

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

---

*Copyright © Anthropic. All rights reserved.*
