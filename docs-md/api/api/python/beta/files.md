# Files

Copy page

Python

# Files

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(FileUploadParams\*\*kwargs)  -> [FileMetadata](api/beta.md)

post/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(FileListParams\*\*kwargs)  -> SyncPage[[FileMetadata](api/beta.md)]

get/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(strfile\_id, FileDownloadParams\*\*kwargs)  -> BinaryResponseContent

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(strfile\_id, FileRetrieveMetadataParams\*\*kwargs)  -> [FileMetadata](api/beta.md)

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [DeletedFile](api/beta.md)

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile: …

id: str

ID of the deleted file.

type: Optional[Literal["file\_deleted"]]

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

"file\_deleted"

class FileMetadata: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

created\_at: datetime

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: str

Original filename of the uploaded file.

maxLength500

minLength1

mime\_type: str

MIME type of the file.

maxLength255

minLength1

size\_bytes: int

Size of the file in bytes.

minimum0

type: Literal["file"]

Object type.

For files, this is always `"file"`.

Accepts one of the following:

"file"

downloadable: Optional[bool]

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
