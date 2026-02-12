# Files

Copy page

Go

# Files

##### [Upload File](api/beta/files/upload.md)

client.Beta.Files.Upload(ctx, params) (\*[FileMetadata](api/beta.md), error)

POST/v1/files

##### [List Files](api/beta/files/list.md)

client.Beta.Files.List(ctx, params) (\*Page[[FileMetadata](api/beta.md)], error)

GET/v1/files

##### [Download File](api/beta/files/download.md)

client.Beta.Files.Download(ctx, fileID, query) (\*Response, error)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

client.Beta.Files.GetMetadata(ctx, fileID, query) (\*[FileMetadata](api/beta.md), error)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

client.Beta.Files.Delete(ctx, fileID, body) (\*[DeletedFile](api/beta.md), error)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

type DeletedFile struct{…}

ID string

ID of the deleted file.

Type DeletedFileTypeoptional

Deleted object type.

For file deletion, this is always `"file_deleted"`.

type FileMetadata struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

CreatedAt Time

RFC 3339 datetime string representing when the file was created.

Filename string

Original filename of the uploaded file.

MimeType string

MIME type of the file.

SizeBytes int64

Size of the file in bytes.

Type File

Object type.

For files, this is always `"file"`.

Downloadable booloptional

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
