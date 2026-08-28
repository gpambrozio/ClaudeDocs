# Upload File

Copy page



cURL

# Upload File

POST/v1/files

Upload File

##### Body (form-data)



file: string

The file to upload

formatbinary



expires\_in\_seconds: optional number

Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

minimum3600

maximum7776000

##### Returns



FileMetadata object{ id, created\_at, filename, 5 more }



id: string

Unique object identifier.

The format and length of IDs may change over time.



created\_at: string

RFC 3339 datetime string representing when the file was created.

formatdate-time



filename: string

Original filename of the uploaded file.

maxLength500

minLength1



mime\_type: string

MIME type of the file.

maxLength255

minLength1



size\_bytes: number

Size of the file in bytes.

minimum0



type: "file"

Object type.

For files, this is always `"file"`.



downloadable: optional boolean

Whether the file can be downloaded.

defaultfalse



expires\_at: optional string or null

RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

formatdate-time



### Upload File

cURL



```shiki
curl https://api.anthropic.com/v1/files \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F 'file=@/path/to/file'
```

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
