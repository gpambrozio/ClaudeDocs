# Files

Copy page

Java

# Files

##### [Upload File](api/beta/files/upload.md)

[FileMetadata](api/beta.md) beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/files

##### [List Files](api/beta/files/list.md)

FileListPage beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/files

##### [Download File](api/beta/files/download.md)

HttpResponse beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

[FileMetadata](api/beta.md) beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

[DeletedFile](api/beta.md) beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile:

String id

ID of the deleted file.

Optional<Type> type

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

FILE\_DELETED("file\_deleted")

class FileMetadata:

String id

Unique object identifier.

The format and length of IDs may change over time.

LocalDateTime createdAt

RFC 3339 datetime string representing when the file was created.

formatdate-time

String filename

Original filename of the uploaded file.

maxLength500

minLength1

String mimeType

MIME type of the file.

maxLength255

minLength1

long sizeBytes

Size of the file in bytes.

minimum0

JsonValue; type "file"constant"file"constant

Object type.

For files, this is always `"file"`.

Accepts one of the following:

FILE("file")

Optional<Boolean> downloadable

Whether the file can be downloaded.