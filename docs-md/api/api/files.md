# Files

Copy page



cURL

# Files

##### [Upload File](api/http/files/upload.md)

POST/v1/files

##### [List Files](api/http/files/list.md)

GET/v1/files

##### [Download File](api/http/files/download.md)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/http/files/retrieve_metadata.md)

GET/v1/files/{file\_id}

##### [Delete File](api/http/files/delete.md)

DELETE/v1/files/{file\_id}

##### Models



DeletedFile object{ id, type }

id: string

ID of the deleted file.



type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

defaultfile\_deleted



FileMetadata object{ id, created\_at, filename, 5 more }



id: string

Unique object identifier.

The format and length of IDs may change over time.



created\_at: string

RFC 3339 datetime string representing when the file was created.

formatdate-time



filename: string

Original filename of the uploaded file.

maxLength500

minLength1



mime\_type: string

MIME type of the file.

maxLength255

minLength1



size\_bytes: number

Size of the file in bytes.

minimum0



type: "file"

Object type.

For files, this is always `"file"`.



downloadable: optional boolean

Whether the file can be downloaded.

defaultfalse



expires\_at: optional string or null

RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

formatdate-time

---

*Copyright © Anthropic. All rights reserved.*
