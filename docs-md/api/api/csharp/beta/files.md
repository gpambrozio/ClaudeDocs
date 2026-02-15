# Files

Copy page

C#

# Files

##### [List Files](api/beta/files/list.md)

[FileListPageResponse](api/beta.md) Beta.Files.List(FileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse Beta.Files.Download(FileDownloadParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta.md) Beta.Files.RetrieveMetadata(FileRetrieveMetadataParamsparameters, CancellationTokencancellationToken = default)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta.md) Beta.Files.Delete(FileDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile:

required string ID

ID of the deleted file.

Type Type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

required string ID

Unique object identifier.

The format and length of IDs may change over time.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing when the file was created.

required string Filename

Original filename of the uploaded file.

required string MimeType

MIME type of the file.

required Long SizeBytes

Size of the file in bytes.

JsonElement Type "file"constant

Object type.

For files, this is always `"file"`.

Boolean Downloadable

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
