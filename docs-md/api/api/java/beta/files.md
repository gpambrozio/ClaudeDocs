# Files

Copy page

Java

# Files

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta.md) beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/files

##### [List Files](api/beta/files/list.md)

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta.md) beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta.md) beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile:

String id

ID of the deleted file.

Optional<Type> type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata:

String id

Unique object identifier.

The format and length of IDs may change over time.

LocalDateTime createdAt

RFC 3339 datetime string representing when the file was created.

String filename

Original filename of the uploaded file.

String mimeType

MIME type of the file.

long sizeBytes

Size of the file in bytes.

JsonValue; type "file"constant"file"constant

Object type.

For files, this is always `"file"`.

Optional<Boolean> downloadable

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
