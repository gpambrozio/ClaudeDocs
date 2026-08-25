# List project attachments

Copy page



# List project attachments

GET/v1/compliance/apps/projects/{project\_id}/attachments

List files and documents attached to a project.

List files and project documents attached to the project referenced by project\_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude\_file\_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude\_proj\_doc\_id} endpoint.

##### Path parameters

project\_id: string

The project ID (tagged ID, e.g., claude\_proj\_abc123)

##### Query parameters



limit: optional number

Maximum results (default: 20, max: 100)

default20

maximum100

minimum1

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Headers

"x-api-key": optional string

##### Returns



data: array of object{ id, created\_at, filename, 4 more } or object{ id, created\_at, filename, 3 more }

List of attachments sorted chronologically by created\_at, tie break by id

One of the following:



ComplianceProjectFileReference object{ id, created\_at, filename, 4 more }

File attachment reference for compliance responses.

id: string

File identifier (e.g., 'claude\_file\_abcd')



created\_at: string

Creation timestamp (RFC 3339 format)

formatdate-time

filename: string

Display name of the file (e.g., 'document.pdf')

md5: string or null

Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

mime\_type: string

MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

size\_bytes: number or null

Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.



type: "project\_file"

Discriminator marking this as a binary file

defaultproject\_file



ComplianceProjectDocReference object{ id, created\_at, filename, 3 more }

Project document attachment reference for compliance responses.

id: string

Project document identifier (e.g., 'claude\_proj\_doc\_abcd')



created\_at: string

Creation timestamp (RFC 3339 format)

formatdate-time

filename: string

Display name of the document (e.g., 'document.txt')



mime\_type: "text/plain"

MIME type of the project document, always set to plain text

defaulttext/plain



type: "project\_doc"

Discriminator marking this as a plain text document

defaultproject\_doc



updated\_at: string or null

Last-modified timestamp of the document. Reserved for future use — currently always null.

formatdate-time

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string or null

To get the next page, use the 'next\_page' from the current response as the 'page' in your next request

### List project attachments

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
