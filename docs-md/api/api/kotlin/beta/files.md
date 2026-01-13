# Files

Copy page

Kotlin

# Files

##### [Upload File](api/beta/files/upload.md)

beta().files().upload(FileUploadParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [FileMetadata](api/beta.md)

post/v1/files

##### [List Files](api/beta/files/list.md)

beta().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : FileListPage

get/v1/files

##### [Download File](api/beta/files/download.md)

beta().files().download(FileDownloadParamsparams = FileDownloadParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : HttpResponse

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta().files().retrieveMetadata(FileRetrieveMetadataParamsparams = FileRetrieveMetadataParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [FileMetadata](api/beta.md)

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta().files().delete(FileDeleteParamsparams = FileDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none()) : [DeletedFile](api/beta.md)

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile:

id: String

ID of the deleted file.

type: Optional<Type>

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

FILE\_DELETED("file\_deleted")

class FileMetadata:

id: String

Unique object identifier.

The format and length of IDs may change over time.

createdAt: LocalDateTime

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: String

Original filename of the uploaded file.

maxLength500

minLength1

mimeType: String

MIME type of the file.

maxLength255

minLength1

sizeBytes: Long

Size of the file in bytes.

minimum0

type: JsonValue; "file"constant"file"constant

Object type.

For files, this is always `"file"`.

Accepts one of the following:

FILE("file")

downloadable: Optional<Boolean>

Whether the file can be downloaded.