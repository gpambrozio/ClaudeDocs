# [Claude docs changes for February 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ac1a472) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ac1a472)]

## Executive Summary
- New comprehensive C# SDK documentation added with 42 files covering Messages API, Models, Skills, Files, and Batches
- Admin API documentation updated with standardized HTTP verb formatting (capitalization)

-----

## API changes

### New Documents

#### [C# SDK - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta)]

New C# SDK beta documentation section covering error models and beta API features.

#### [C# SDK - Beta Files](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/files.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/files)]

Documentation for C# SDK beta file operations including upload, download, retrieval, and deletion.

##### [Delete a File](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/files/delete.md)

C# SDK documentation for deleting files via the beta Files API.

##### [Download File Content](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/files/download.md)

C# SDK documentation for downloading file content from the beta Files API.

##### [List Files](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/files/list.md)

C# SDK documentation for listing files via the beta Files API.

##### [Retrieve File Metadata](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/files/retrieve_metadata.md)

C# SDK documentation for retrieving file metadata from the beta Files API.

#### [C# SDK - Beta Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/messages)]

Comprehensive C# SDK documentation for the beta Messages API including message creation, token counting, and streaming.

##### [Beta Messages Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches.md)

C# SDK documentation for batch message operations in beta.

##### [Cancel a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/cancel.md)

C# SDK documentation for canceling message batches.

##### [Create a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/create.md)

C# SDK documentation for creating message batches for bulk processing.

##### [Delete a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/delete.md)

C# SDK documentation for deleting message batches.

##### [List Message Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/list.md)

C# SDK documentation for listing message batches.

##### [Retrieve Message Batch Results](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/results.md)

C# SDK documentation for retrieving results from message batches.

##### [Retrieve a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/batches/retrieve.md)

C# SDK documentation for retrieving message batch details.

##### [Count Tokens in a Message](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/count_tokens.md)

C# SDK documentation for counting tokens in messages before sending them.

##### [Create a Message](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/messages/create.md)

C# SDK documentation for creating messages with the beta Messages API.

#### [C# SDK - Beta Models](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/models.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/models)]

C# SDK documentation for working with Claude models in beta.

##### [List Models](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/models/list.md)

C# SDK documentation for listing available Claude models.

##### [Retrieve Model Information](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/models/retrieve.md)

C# SDK documentation for retrieving detailed information about specific models.

#### [C# SDK - Beta Skills](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/skills)]

C# SDK documentation for managing skills in the beta API.

##### [Create a Skill](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/create.md)

C# SDK documentation for creating new skills.

##### [Delete a Skill](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/delete.md)

C# SDK documentation for deleting skills.

##### [List Skills](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/list.md)

C# SDK documentation for listing available skills.

##### [Retrieve a Skill](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/retrieve.md)

C# SDK documentation for retrieving skill details.

##### [Skill Versions](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/versions.md)

C# SDK documentation for managing skill versions.

##### [Create a Skill Version](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/versions/create.md)

C# SDK documentation for creating new versions of skills.

##### [Delete a Skill Version](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/versions/delete.md)

C# SDK documentation for deleting skill versions.

##### [List Skill Versions](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/versions/list.md)

C# SDK documentation for listing versions of a skill.

##### [Retrieve a Skill Version](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/beta/skills/versions/retrieve.md)

C# SDK documentation for retrieving details about a specific skill version.

#### [C# SDK - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages.md) [[Source](https://platform.claude.com/docs/en/api/csharp/messages)]

Comprehensive C# SDK documentation for the stable Messages API including all message operations and model definitions.

##### [Messages Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches.md)

C# SDK documentation for batch operations in the stable Messages API.

##### [Cancel a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/cancel.md)

C# SDK documentation for canceling message batches in the stable API.

##### [Create a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/create.md)

C# SDK documentation for creating message batches in the stable API.

##### [Delete a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/delete.md)

C# SDK documentation for deleting message batches in the stable API.

##### [List Message Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/list.md)

C# SDK documentation for listing message batches in the stable API.

##### [Retrieve Message Batch Results](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/results.md)

C# SDK documentation for retrieving results from message batches in the stable API.

##### [Retrieve a Message Batch](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/batches/retrieve.md)

C# SDK documentation for retrieving message batch details in the stable API.

##### [Count Tokens in a Message](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/count_tokens.md)

C# SDK documentation for counting tokens in messages in the stable API.

##### [Create a Message](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/messages/create.md)

C# SDK documentation for creating messages with detailed parameter descriptions and example code.

#### [C# SDK - Models](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/models.md) [[Source](https://platform.claude.com/docs/en/api/csharp/models)]

C# SDK documentation for working with Claude models in the stable API.

##### [List Models](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/models/list.md)

C# SDK documentation for listing available models in the stable API.

##### [Retrieve Model Information](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/csharp/models/retrieve.md)

C# SDK documentation for retrieving model details in the stable API.

### Changed documents

#### [Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* HTTP method formatting standardized - changed from lowercase to uppercase (GET, POST, DELETE). [[lines 15, 39, 43, 47, 51, 115, 119, 123, 127, 177, 181](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin.md?plain=1#L15)]

#### [API Keys - List](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/list.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

#### [API Keys - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

#### [API Keys - Update](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/api_keys/update.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

#### [Cost Report - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/cost_report/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/cost_report/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]

#### [Invites - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/create.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/create)]

#### [Invites - Delete](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

* HTTP method formatting standardized to uppercase DELETE. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/delete.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/delete)]

#### [Invites - List](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/list)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/list.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/list)]

#### [Invites - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/invites/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/invites/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/invites/retrieve)]

#### [Organizations - Me](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/organizations/me.md) [[Source](https://platform.claude.com/docs/en/api/admin/organizations/me)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/organizations/me.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/organizations/me)]

#### [Usage Report - Retrieve Claude Code](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/usage_report/retrieve_claude_code.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/usage_report/retrieve_claude_code.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]

#### [Usage Report - Retrieve Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/usage_report/retrieve_messages.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

#### [Users - Delete](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/delete)]

* HTTP method formatting standardized to uppercase DELETE. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/delete.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/users/delete)]

#### [Users - List](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/list)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/list.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/users/list)]

#### [Users - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/users/retrieve)]

#### [Users - Update](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/users/update)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/users/update.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/users/update)]

#### [Workspaces - Archive](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/archive.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/archive.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/archive)]

#### [Workspaces - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/create.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

#### [Workspaces - List](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/list.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/list)]

#### [Workspaces - Members - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/create.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/create)]

#### [Workspaces - Members - Delete](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/delete.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete)]

* HTTP method formatting standardized to uppercase DELETE. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/delete.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/delete)]

#### [Workspaces - Members - List](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/list)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/list.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/list)]

#### [Workspaces - Members - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/retrieve)]

#### [Workspaces - Members - Update](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/members/update.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/members/update)]

#### [Workspaces - Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

* HTTP method formatting standardized to uppercase GET. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/retrieve.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/retrieve)]

#### [Workspaces - Update](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

* HTTP method formatting standardized to uppercase POST. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/ac1a472/docs-md/api/api/admin/workspaces/update.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]
