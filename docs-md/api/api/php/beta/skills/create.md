# Create Skill

Copy page



PHP

# Create Skill

$client->beta->skills->create(list<string> files, ?string displayTitle, ?list<AnthropicBeta> betas): [SkillNewResponse](api/beta/skills.md)

POST/v1/skills

Create Skill

##### ParametersExpand Collapse



files: list<string>

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.



displayTitle?:optional string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[SkillNewResponse](api/beta/skills.md)



string id

Unique identifier for the skill.

The format and length of IDs may change over time.

string createdAt

ISO 8601 timestamp of when the skill was created.



?string displayTitle

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



?string latestVersion

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



string source

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



string type

Object type.

For Skills, this is always `"skill"`.

string updatedAt

ISO 8601 timestamp of when the skill was last updated.

Create Skill

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$skill = $client->beta->skills->create(
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  displayTitle: 'display_title',
  betas: ['message-batches-2024-09-24'],
);

var_dump($skill);
```

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
