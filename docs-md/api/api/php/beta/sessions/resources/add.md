# Add Session Resource

Copy page

SDK language

PHP

# Add Session Resource

$client->beta->sessions->resources->add(string sessionID, string fileID, [Type](api/beta/sessions/resources/add.md) type, ?string mountPath, ?list<AnthropicBeta> betas): [ManagedAgentsFileResource](api/beta.md)

POST/v1/sessions/{session\_id}/resources

Add Session Resource

##### ParametersExpand Collapse

sessionID: string

fileID: string

ID of a previously uploaded file.

type: [Type](api/beta/sessions/resources/add.md)

mountPath?:optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[ManagedAgentsFileResource](api/beta.md)

string id

\Datetime createdAt

A timestamp in RFC 3339 format

string fileID

string mountPath

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

Add Session Resource

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsFileResource = $client->beta->sessions->resources->add(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
  type: 'file',
  mountPath: '/uploads/receipt.pdf',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaManagedAgentsFileResource);
```

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
