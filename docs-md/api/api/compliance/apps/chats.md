# Chats

Copy page



# Chats

##### [List chats](api/http/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/http/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

##### Models



ChatListResponse object{ id, created\_at, deleted\_at, 8 more }

Chat metadata for listing chats (without messages).



ChatDeleteResponse object{ id, type }

Response for deleting a Claude chat.

id: string

The ID of the Claude chat that was deleted



type: optional "claude\_chat\_deleted"

Constant string confirming deletion

defaultclaude\_chat\_deleted

#### Chats[Messages](api/http/compliance/apps/chats/messages.md)

##### [Get chat messages](api/http/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

#### Chats[Files](api/http/compliance/apps/chats/files.md)

##### [Get file metadata](api/http/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/http/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/http/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

#### Chats[Generated Files](api/http/compliance/apps/chats/generated_files.md)

##### [Get Claude-generated file metadata](api/http/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/http/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

---

*Copyright © Anthropic. All rights reserved.*
