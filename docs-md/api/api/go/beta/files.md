# Files

Copy page

Go

# Files

##### [Upload File](api/beta/files/upload.md)

client.Beta.Files.Upload(ctx, params) (\*[FileMetadata](api/beta.md), error)

post/v1/files

##### [List Files](api/beta/files/list.md)

client.Beta.Files.List(ctx, params) (\*Page[[FileMetadata](api/beta.md)], error)

get/v1/files

##### [Download File](api/beta/files/download.md)

client.Beta.Files.Download(ctx, fileID, query) (\*Response, error)

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

client.Beta.Files.GetMetadata(ctx, fileID, query) (\*[FileMetadata](api/beta.md), error)

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

client.Beta.Files.Delete(ctx, fileID, body) (\*[DeletedFile](api/beta.md), error)

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

type DeletedFile struct{…}

ID string

ID of the deleted file.

Type DeletedFileTypeoptional

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

const DeletedFileTypeFileDeleted DeletedFileType = "file\_deleted"

type FileMetadata struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

CreatedAt Time

RFC 3339 datetime string representing when the file was created.

formatdate-time

Filename string

Original filename of the uploaded file.

maxLength500

minLength1

MimeType string

MIME type of the file.

maxLength255

minLength1

SizeBytes int64

Size of the file in bytes.

minimum0

Type File

Object type.

For files, this is always `"file"`.

Accepts one of the following:

const FileFile File = "file"

Downloadable booloptional

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
