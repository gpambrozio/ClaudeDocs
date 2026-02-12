# Files

Copy page

TypeScript

# Files

##### [Upload File](api/beta/files/upload.md)

client.beta.files.upload(FileUploadParams { file, betas } params, RequestOptionsoptions?): [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

POST/v1/files

##### [List Files](api/beta/files/list.md)

client.beta.files.list(FileListParams { after\_id, before\_id, limit, betas } params?, RequestOptionsoptions?): Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 4 more } >

GET/v1/files

##### [Download File](api/beta/files/download.md)

client.beta.files.download(stringfileID, FileDownloadParams { betas } params?, RequestOptionsoptions?): Response

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

client.beta.files.retrieveMetadata(stringfileID, FileRetrieveMetadataParams { betas } params?, RequestOptionsoptions?): [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

client.beta.files.delete(stringfileID, FileDeleteParams { betas } params?, RequestOptionsoptions?): [DeletedFile](api/beta.md) { id, type }

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

DeletedFile { id, type }

id: string

ID of the deleted file.

type?: "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

FileMetadata { id, created\_at, filename, 4 more }

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

downloadable?: boolean

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
