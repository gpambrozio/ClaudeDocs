# Delete File

Copy page



PHP

# Delete File

$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): [DeletedFile](api/beta.md)

DELETE/v1/files/{file\_id}

Delete File

##### ParametersExpand Collapse

fileID: string

ID of the File.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[DeletedFile](api/beta.md)

string id

ID of the deleted file.



?Type type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Delete File

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$deletedFile = $client->beta->files->delete(
  'file_id', betas: ['message-batches-2024-09-24']
);

var_dump($deletedFile);
```

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
