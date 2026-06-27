# Files

Copy page



PHP

# Files

##### [Upload File](api/beta/files/upload.md)

$client->beta->files->upload(string file, ?list<AnthropicBeta> betas): [FileMetadata](api/beta/files.md)

POST/v1/files

##### [List Files](api/beta/files/list.md)

$client->beta->files->list(?string afterID, ?string beforeID, ?int limit, ?string scopeID, ?list<AnthropicBeta> betas): Page<[FileMetadata](api/beta/files.md)>

GET/v1/files

##### [Download File](api/beta/files/download.md)

$client->beta->files->download(string fileID, ?list<AnthropicBeta> betas): download

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

$client->beta->files->retrieveMetadata(string fileID, ?list<AnthropicBeta> betas): [FileMetadata](api/beta/files.md)

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

$client->beta->files->delete(string fileID, ?list<AnthropicBeta> betas): [DeletedFile](api/beta/files.md)

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse



[BetaFileScope](api/beta/files.md)

string id

The ID of the scoping resource (e.g., the session ID).

"session" type

The type of scope (e.g., `"session"`).



[DeletedFile](api/beta/files.md)

string id

ID of the deleted file.



?Type type

Deleted object type.

For file deletion, this is always `"file_deleted"`.



[FileMetadata](api/beta/files.md)



string id

Unique object identifier.

The format and length of IDs may change over time.

\Datetime createdAt

RFC 3339 datetime string representing when the file was created.

string filename

Original filename of the uploaded file.

string mimeType

MIME type of the file.

int sizeBytes

Size of the file in bytes.



"file" type

Object type.

For files, this is always `"file"`.

?bool downloadable

Whether the file can be downloaded.

?[BetaFileScope](api/beta/files.md) scope

The scope of this file, indicating the context in which it was created (e.g., a session).

---

*Copyright © Anthropic. All rights reserved.*
