# Files API

Copy page



The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) to provide inputs (for example, datasets and documents) and then download outputs (for example, charts). You can [explore the API reference directly](api/files/upload.md), in addition to this guide.

##  File type support

Referencing a `file_id` in a Messages request is supported on all models that support the given file type. [Images](build-with-claude/vision.md) are supported on all current Claude models. For [PDFs](build-with-claude/pdf-support.md) and [other file types with the code execution tool](agents-and-tools/tool-use/code-execution-tool.md), see the linked pages for model support.

##  How the Files API works

The Files API provides a create-once, use-many-times approach for working with files:

- **Upload files** to Anthropic's secure storage and receive a unique `file_id`
- **Download files** that are created by skills or the code execution tool
- **Reference files** in [Messages](api/messages/create.md) requests using the `file_id` instead of re-uploading content
- **Manage your files** with list, retrieve, and delete operations

##  How to use the Files API

###  Uploading a file

Upload a file to be referenced in future API calls:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
uploaded = client.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
)
file_id = uploaded.id
print(file_id)
```

The response from uploading a file includes:

Response



```shiki
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1024000,
  "created_at": "2025-01-01T00:00:00Z",
  "downloadable": false,
  "expires_at": null
}
```

`downloadable` is `false` for files you upload. Only files created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) can be downloaded. See [Downloading a file](#downloading-a-file).

###  Using a file in messages

Once uploaded, reference the file by passing the `id` from the upload response as `file_id`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                {
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": file_id,
                    },
                },
            ],
        }
    ],
)
print(response)
```

###  File types and content blocks

The Files API supports different file types that correspond to different content block types:

| File type | MIME type | Content block type | Use case |
| --- | --- | --- | --- |
| PDF | `application/pdf` | `document` | Text analysis, document processing |
| Plain text | `text/plain` | `document` | Text analysis, processing |
| Images | `image/jpeg`, `image/png`, `image/gif`, `image/webp` | `image` | Image analysis, visual tasks |
| [Datasets, others](agents-and-tools/tool-use/code-execution-tool.md) | Varies | `container_upload` | Analyze data, create visualizations |

####  Document blocks

For PDFs and text files, use the `document` content block:

```shiki
{
  "type": "document",
  "source": {
    "type": "file",
    "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
  },
  "title": "Document Title", // Optional
  "context": "Context about the document", // Optional
  "citations": { "enabled": true } // Optional, enables citations
}
```



####  Image blocks

For images, use the `image` content block:

```shiki
{
  "type": "image",
  "source": {
    "type": "file",
    "file_id": "file_011CPMxVD3fHLUhvTqtsQA5w"
  }
}
```



####  Container upload blocks

To send a file to the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md), use the `container_upload` content block:

```shiki
{
  "type": "container_upload",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
}
```



###  Working with other file formats

For file types that the `document` block doesn't support (for example, .docx and .xlsx), convert the files to plain text and include the content directly in your message. Files that are already plain text, such as .csv and .md files, can either be read in this way or uploaded through the Files API with an explicit `text/plain` content type. To analyze datasets instead of reading them as text, upload them for the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) using a `container_upload` block.

The following examples read a text file and send its contents as plain text:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# Read the text file
with open("document.txt") as f:
    text_content = f.read()

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Here's the document content:\n\n{text_content}\n\nPlease summarize this document.",
                }
            ],
        }
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

###  Managing files

####  List files

Retrieve a list of your uploaded files. The endpoint is paginated: each request returns up to `limit` files (20 by default, and at most 1,000), and the response's `next_page` cursor fetches the next page when passed back as the `page` parameter. Files are ordered newest first. See the [List Files API reference](api/files/list.md). The SDKs return the first page and provide auto-pagination helpers. The CLI example bounds the total with `--max-items`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
files = client.files.list()
print(files)
```

To check a known set of files in one request instead of paging, pass up to 100 file IDs as `ids[]` query parameters. An `ids[]` request always returns a single page (`next_page` is `null`), and any ID that does not resolve to a file in your workspace is silently omitted from `data`; compare the returned IDs against the requested IDs to detect misses. `ids[]` cannot be combined with `page` or `limit`.

####  Get file metadata

Retrieve information about a specific file:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file = client.files.retrieve_metadata(file_id)
print(file)
```

####  Delete a file

Remove a file from your workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client.files.delete(file_id)
```

###  Downloading a file

Download files that were created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md). Files you upload cannot be downloaded. The `file_id` of a generated file appears in the [`bash_code_execution_tool_result` content block](agents-and-tools/tool-use/code-execution-tool.md) of the Messages response that created it:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file_content = client.files.download(file_id)

file_content.write_to_file("downloaded_file.txt")
```

##  File storage and limits

###  Storage limits

- **Maximum file size:** 500 MB per file
- **Total storage:** 1 TB per organization

###  File lifecycle

- Files are scoped to the workspace they were uploaded in. Any request in the same workspace can reference them; never accept file IDs from untrusted sources (see the [workspace access warning](#workspace-scoped-access))
- Files cannot be modified or renamed after upload. To change a file's content, upload a new file and delete the old one
- Files persist until you delete them with the `DELETE /v1/files/{file_id}` endpoint or they reach their `expires_at`
- Deleted files cannot be recovered
- Files are inaccessible through the API shortly after deletion, but they may persist in active Messages API calls and associated tool uses
- Files that users delete will be deleted in accordance with Anthropic's [data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data). For ZDR eligibility across all features, see [API and data retention](manage-claude/api-and-data-retention.md)

###  File expiration

To have a file expire automatically, include an `expires_in_seconds` form field when you upload it. The value is an integer number of seconds between 3,600 (1 hour) and 7,776,000 (90 days). The resulting `expires_at` timestamp (RFC 3339) appears on every file response and is `null` for files uploaded without an expiration. Expiration is set once at upload and cannot be changed.

When a file reaches its `expires_at`:

- Downloading its content (`GET /v1/files/{file_id}/content`) returns a 404 error
- A Messages request that references the file fails before inference
- Its metadata (`GET /v1/files/{file_id}`) remains readable for up to 30 days, with `expires_at` in the past
- It continues to appear in list responses during that window; compare `expires_at` to the current time to filter expired files

Deleting an expired file with `DELETE /v1/files/{file_id}` removes its metadata immediately instead of waiting for the 30-day window to elapse.

###  Audit logging

If your organization has the [Compliance API](manage-claude/compliance-api.md) enabled, its [Activity Feed](manage-claude/compliance-activity-feed.md) records Files API operations made with a Claude API key or from the Claude Console: each upload (`POST /v1/files`), content download (`GET /v1/files/{file_id}/content`), and deletion (`DELETE /v1/files/{file_id}`) appears as a `platform_file_uploaded`, `platform_file_content_downloaded`, or `platform_file_deleted` activity. Listing files and retrieving file metadata are not recorded. Operations that occur while the Compliance API is off are not recorded and cannot be recovered later, so [set up the Compliance API](manage-claude/compliance-api-access.md) before you rely on this audit trail. On [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), audit file operations with AWS CloudTrail data events instead.

##  Migrate from `files-api-2025-04-14`

The Files API is out of beta and needs no beta header. Migrating off `files-api-2025-04-14` is optional: requests that still send it keep working and keep returning the beta response shapes, so an existing integration keeps working until you change it. Removing the header switches those requests to the shapes documented on this page:

|  | With `files-api-2025-04-14` | Without the header |
| --- | --- | --- |
| List response | `{ data, has_more, first_id, last_id }` | `{ data, next_page }`; pass `next_page` back as the `page` query parameter |
| List cursors | `before_id`, `after_id` | `page`, or up to 100 `ids[]` (`before_id` and `after_id` return a 400 error) |
| `expires_at` on file objects | Not returned | Always present; `null` when the file has no expiration |
| `Content-Type` on the uploaded file part | Required | Optional; the type is detected when omitted |

To migrate:

1. **Remove the beta header.** Drop `anthropic-beta: files-api-2025-04-14` from your requests. In the SDKs, call `client.files` instead of `client.beta.files`; keeping `client.beta.files` works only on the [SDK releases that no longer send the header](#sdk-beta-namespace). Earlier releases send it from `client.beta.files` even with no `betas` argument.
2. **Update pagination.** Replace `after_id`/`before_id` loops with the `page`/`next_page` cursor, or use the SDK auto-pagination helpers shown in [Managing files](#managing-files).
3. **Read `expires_at`.** The field appears only without the header; `null` means the file has no expiration (see [File expiration](#file-expiration)).

###  SDK beta namespace

Starting with Python SDK 1.2.0, TypeScript SDK 0.122.0, Go SDK 1.68.0, Java SDK 2.59.0, Ruby SDK 1.67.0, and C# SDK 12.44.0, `client.beta.files` no longer sends `files-api-2025-04-14` and returns the same shapes as `client.files`, with `Beta`-prefixed type names. It accepts a `betas` argument for Files features that are still in beta, such as `scope_id` filtering under a [Managed Agents](managed-agents/files.md) beta header. Earlier SDK releases are typed to the beta shapes; if you depend on those types, stay on an earlier release until you migrate.

Requests that carry `anthropic-beta: managed-agents-2026-04-01` without `files-api-2025-04-14` receive the shapes on this page with one compatibility affordance on `GET /v1/files`: `before_id` and `after_id` are still accepted (not combinable with `page` or `ids[]`), and the list response includes `has_more`, `first_id`, and `last_id` alongside `next_page`. Later Managed Agents beta versions receive the plain shape.

##  Error handling

Common errors when using the Files API include:

- **File not found (404):** The specified `file_id` doesn't exist or you don't have access to it
- **Invalid file type (400):** The file type doesn't match the content block type (for example, using an image file in a document block)
- **Not downloadable (400):** Files you upload have `"downloadable": false` and cannot be downloaded. Only files created by skills or the code execution tool can be downloaded
- **Exceeds context window size (400):** The file is larger than the context window size (for example, using a 500 MB plain text file in a `/v1/messages` request)
- **Invalid filename (400):** The file name doesn't meet the length requirements (1-255 characters) or contains forbidden characters (`<`, `>`, `:`, `"`, `|`, `?`, `*`, `\`, `/`, or Unicode characters 0-31)
- **File too large (413):** File exceeds the 500 MB limit
- **Storage limit exceeded (400):** Your organization has reached the 1 TB storage limit

Output



```shiki
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "File `file_011CNha8iCJcU1wXNR6q4V8w` not found."
  },
  "request_id": "req_011CQFYcrRp7mCHLDsAYT8Qt"
}
```

##  Usage and billing

Files API operations are free:

- Uploading files
- Downloading files
- Listing files
- Getting file metadata
- Deleting files

File content used in Messages requests is priced as input tokens.

###  Rate limits

File-related API calls are limited to approximately 500 requests per minute. To request a higher limit, [contact sales](mailto:sales@anthropic.com).

##  Next steps



[PDF support](build-with-claude/pdf-support.md)

Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.



[Code execution tool](agents-and-tools/tool-use/code-execution-tool.md)

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.



[Vision](build-with-claude/vision.md)

Process and analyze visual input and generate text and code from images.

## Compatibility

|  |  |
| --- | --- |
| Supported platforms | - Claude API - Claude Platform on AWSBeta - Microsoft Foundry[1](#compat-fn-1)Beta |

1. On [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md), the Files API requires a [Hosted on Anthropic deployment](build-with-claude/claude-in-microsoft-foundry.md). [↩](#compat-fnref-1)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
