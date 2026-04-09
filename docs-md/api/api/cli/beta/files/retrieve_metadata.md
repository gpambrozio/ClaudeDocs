# Get File Metadata

Copy page

CLI

# Get File Metadata

$ ant beta:files retrieve-metadata

GET/v1/files/{file\_id}

Get File Metadata

##### ParametersExpand Collapse

--file-id: string

ID of the File.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

file\_metadata: object { id, created\_at, filename, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created\_at: string

RFC 3339 datetime string representing when the file was created.

filename: string

Original filename of the uploaded file.

mime\_type: string

MIME type of the file.

size\_bytes: number

Size of the file in bytes.

type: "file"

Object type.

For files, this is always `"file"`.

downloadable: optional boolean

Whether the file can be downloaded.

scope: optional object { id, type }

The scope of this file, indicating the context in which it was created (e.g., a session).

id: string

The ID of the scoping resource (e.g., the session ID).

type: "session"

The type of scope (e.g., `"session"`).

Get File Metadata

CLI

```shiki
ant beta:files retrieve-metadata \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

Response 200

```shiki
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
```

##### Returns Examples

Response 200

```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
