# Files

Copy page

Ruby

# Files

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(\*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

post/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 4 more } >

get/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(file\_id, \*\*kwargs) -> StringIO

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta.md) { id, type }

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file\_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

:file\_deleted

class FileMetadata { id, created\_at, filename, 4 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: String

Original filename of the uploaded file.

maxLength500

minLength1

mime\_type: String

MIME type of the file.

maxLength255

minLength1

size\_bytes: Integer

Size of the file in bytes.

minimum0

type: :file

Object type.

For files, this is always `"file"`.

Accepts one of the following:

:file

downloadable: bool

Whether the file can be downloaded.

---

*Copyright © Anthropic. All rights reserved.*
