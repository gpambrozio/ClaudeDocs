# List Files

Copy page

CLI

# List Files

$ ant beta:files list

GET/v1/files

List Files

##### ParametersExpand Collapse

--after-id: optional string

Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

--before-id: optional string

Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

--limit: optional number

Query param: Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

--scope-id: optional string

Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaFileListResponse: object { data, first\_id, has\_more, last\_id }

data: array of [FileMetadata](api/beta.md) { id, created\_at, filename, 5 more }

List of file metadata objects.

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

first\_id: optional string

ID of the first file in this page of results.

has\_more: optional boolean

Whether there are more results available.

last\_id: optional string

ID of the last file in this page of results.

List Files

CLI

```shiki
ant beta:files list \
  --api-key my-anthropic-api-key
```

Response 200

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
