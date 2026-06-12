# List Files

Copy page

SDK language

PHP

# List Files

$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<[FileMetadata](api/beta.md)>

GET/v1/files

List Files

##### ParametersExpand Collapse

afterID?:optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

beforeID?:optional string

ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



limit?:optional int

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

scopeID?:optional string

Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[FileMetadata](api/beta.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

\Datetime createdAt

RFC 3339 datetime string representing when the file was created.

string filename

Original filename of the uploaded file.

string mimeType

MIME type of the file.

int sizeBytes

Size of the file in bytes.



"file" type

Object type.

For files, this is always `"file"`.

?bool downloadable

Whether the file can be downloaded.

?[BetaFileScope](api/beta.md) scope

The scope of this file, indicating the context in which it was created (e.g., a session).

List Files

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->files->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  scopeID: 'scope_id',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

---

*Copyright © Anthropic. All rights reserved.*
