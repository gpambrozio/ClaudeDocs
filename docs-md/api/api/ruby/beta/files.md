# Files

Copy page

Ruby

# Files

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(\*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 5 more }

POST/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 5 more } >

GET/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(file\_id, \*\*kwargs) -> StringIO

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 5 more }

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta.md) { id, type }

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class BetaFileScope { id, type }

id: String

The ID of the scoping resource (e.g., the session ID).

type: :session

The type of scope (e.g., `"session"`).

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file\_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata { id, created\_at, filename, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

filename: String

Original filename of the uploaded file.

mime\_type: String

MIME type of the file.

size\_bytes: Integer

Size of the file in bytes.

type: :file

Object type.

For files, this is always `"file"`.

downloadable: bool

Whether the file can be downloaded.

scope: [BetaFileScope](api/beta.md) { id, type }

The scope of this file, indicating the context in which it was created (e.g., a session).

id: String

The ID of the scoping resource (e.g., the session ID).

type: :session

The type of scope (e.g., `"session"`).

---

*Copyright © Anthropic. All rights reserved.*
