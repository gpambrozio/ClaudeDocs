# Create Skill Version

Copy page

SDK language

PHP

# Create Skill Version

$client->beta->skills->versions->create(string skillID, ?list<string> files, ?list<AnthropicBeta> betas): [VersionNewResponse](api/beta.md)

POST/v1/skills/{skill\_id}/versions

Create Skill Version

##### ParametersExpand Collapse

skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.

files?:optional list<string>

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[VersionNewResponse](api/beta.md)

string id

Unique identifier for the skill version.

The format and length of IDs may change over time.

string createdAt

ISO 8601 timestamp of when the skill version was created.

string description

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

string directory

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

string name

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

string skillID

Identifier for the skill that this version belongs to.

string type

Object type.

For Skill Versions, this is always `"skill_version"`.

string version

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Create Skill Version

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$version = $client->beta->skills->versions->create(
  'skill_id',
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  betas: ['message-batches-2024-09-24'],
);

var_dump($version);
```

Response 200



```shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

---

*Copyright © Anthropic. All rights reserved.*
