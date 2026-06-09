# Download File

Copy page

SDK language

PHP

# Download File

$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download

GET/v1/files/{file\_id}/content

Download File

##### ParametersExpand Collapse

fileID: string

ID of the File.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

mixed

Download File

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$response = $client->beta->files->download(
  'file_id', betas: ['message-batches-2024-09-24']
);

var_dump($response);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
