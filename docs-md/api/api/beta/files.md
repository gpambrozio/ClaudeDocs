# Files

Copy page

cURL

# Files

##### [Upload File](api/beta/files/upload.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

GET/v1/files

##### [Download File](api/beta/files/download.md)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

DeletedFile = object { id, type }

id: string

ID of the deleted file.

type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata = object { id, created\_at, filename, 4 more }

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

---

*Copyright © Anthropic. All rights reserved.*
