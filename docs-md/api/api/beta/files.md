# Files

Copy page



cURL

# Files

##### [Upload File](api/http/beta/files/upload.md)

POST/v1/files

##### [List Files](api/http/beta/files/list.md)

GET/v1/files

##### [Download File](api/http/beta/files/download.md)

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/http/beta/files/retrieve_metadata.md)

GET/v1/files/{file\_id}

##### [Delete File](api/http/beta/files/delete.md)

DELETE/v1/files/{file\_id}

##### Models



BetaDeletedFile object{ id, type }

id: string

ID of the deleted file.



type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

defaultfile\_deleted



BetaFileMetadata object{ id, created\_at, filename, 6 more }



BetaFileScope object{ id, type }

id: string

The ID of the scoping resource (e.g., the session ID).

type: "session"

The type of scope (e.g., `"session"`).

---

*Copyright © Anthropic. All rights reserved.*
