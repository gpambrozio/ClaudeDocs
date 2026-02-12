# Files

Copy page

Python

# Files

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(FileUploadParams\*\*kwargs)  -> [FileMetadata](api/beta.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(FileListParams\*\*kwargs)  -> SyncPage[[FileMetadata](api/beta.md)]

GET/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(strfile\_id, FileDownloadParams\*\*kwargs)  -> BinaryResponseContent

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(strfile\_id, FileRetrieveMetadataParams\*\*kwargs)  -> [FileMetadata](api/beta.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(strfile\_id, FileDeleteParams\*\*kwargs)  -> [DeletedFile](api/beta.md)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile: …

id: str

ID of the deleted file.

type: Optional[Literal["file\_deleted"]]

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

created\_at: datetime

RFC 3339 datetime string representing when the file was created.

filename: str

Original filename of the uploaded file.

mime\_type: str

MIME type of the file.

size\_bytes: int

Size of the file in bytes.

type: Literal["file"]

Object type.

For files, this is always `"file"`.

downloadable: Optional[bool]

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
