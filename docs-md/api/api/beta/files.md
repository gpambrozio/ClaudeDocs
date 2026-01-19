# Files

Copy page

cURL

# Files

##### [Upload File](api/beta/files/upload.md)

post/v1/files

##### [List Files](api/beta/files/list.md)

get/v1/files

##### [Download File](api/beta/files/download.md)

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

DeletedFile = object { id, type }

id: string

ID of the deleted file.

type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file\_deleted"

FileMetadata = object { id, created\_at, filename, 4 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created\_at: string

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: string

Original filename of the uploaded file.

maxLength500

minLength1

mime\_type: string

MIME type of the file.

maxLength255

minLength1

size\_bytes: number

Size of the file in bytes.

minimum0

type: "file"

Object type.

For files, this is always `"file"`.

Accepts one of the following:

"file"

downloadable: optional boolean

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
