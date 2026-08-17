# Files API

Copy page



The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) to provide inputs (for example, datasets and documents) and then download outputs (for example, charts). You can [explore the API reference directly](api/beta/files/upload.md), in addition to this guide.

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
uploaded = client.beta.files.upload(
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
  "downloadable": false
}
```

`downloadable` is `false` for files you upload. Only files created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) can be downloaded. See [Downloading a file](#downloading-a-file).

###  Using a file in messages

Once uploaded, reference the file by passing the `id` from the upload response as `file_id`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.beta.messages.create(
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
    betas=["files-api-2025-04-14"],
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

Retrieve a list of your uploaded files. The endpoint is paginated: each request returns up to `limit` files (20 by default), and the `before_id` and `after_id` parameters fetch the adjacent page. See the [List Files API reference](api/beta/files/list.md). The SDKs return the first page and provide auto-pagination helpers. The CLI example bounds the total with `--max-items`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
files = client.beta.files.list()
print(files)
```

####  Get file metadata

Retrieve information about a specific file:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file = client.beta.files.retrieve_metadata(file_id)
print(file)
```

####  Delete a file

Remove a file from your workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client.beta.files.delete(file_id)
```

###  Downloading a file

Download files that were created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md). Files you upload cannot be downloaded. The `file_id` of a generated file appears in the [`bash_code_execution_tool_result` content block](agents-and-tools/tool-use/code-execution-tool.md) of the Messages response that created it:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file_content = client.beta.files.download(file_id)

file_content.write_to_file("downloaded_file.txt")
```

##  File storage and limits

###  Storage limits

- **Maximum file size:** 500 MB per file
- **Total storage:** 500 GB per organization

###  File lifecycle

- Files are scoped to the workspace of the API key that uploaded them. Any API key in the same workspace can reference them; never accept file IDs from untrusted sources (see the [workspace access warning](#workspace-scoped-access))
- Files cannot be modified or renamed after upload. To change a file's content, upload a new file and delete the old one
- Files persist until you delete them with the `DELETE /v1/files/{file_id}` endpoint
- Deleted files cannot be recovered
- Files are inaccessible through the API shortly after deletion, but they may persist in active Messages API calls and associated tool uses
- Files that users delete will be deleted in accordance with Anthropic's [data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data). For ZDR eligibility across all features, see [API and data retention](manage-claude/api-and-data-retention.md)

##  Error handling

Common errors when using the Files API include:

- **File not found (404):** The specified `file_id` doesn't exist or you don't have access to it
- **Invalid file type (400):** The file type doesn't match the content block type (for example, using an image file in a document block)
- **Not downloadable (400):** Files you upload have `"downloadable": false` and cannot be downloaded. Only files created by skills or the code execution tool can be downloaded
- **Exceeds context window size (400):** The file is larger than the context window size (for example, using a 500 MB plain text file in a `/v1/messages` request)
- **Invalid filename (400):** The file name doesn't meet the length requirements (1-255 characters) or contains forbidden characters (`<`, `>`, `:`, `"`, `|`, `?`, `*`, `\`, `/`, or Unicode characters 0-31)
- **File too large (413):** File exceeds the 500 MB limit
- **Storage limit exceeded (400):** Your organization has reached the 500 GB storage limit

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

During the beta period:

- File-related API calls are limited to approximately 100 requests per minute
- [Contact us](/cdn-cgi/l/email-protection#87f4e6ebe2f4c7e6e9f3eff5e8f7eee4a9e4e8ea) if you need higher limits for your use case

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
| Supported platforms | - Claude APIBeta - Claude Platform on AWSBeta - Microsoft Foundry[1](#compat-fn-1)Beta |

1. On [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md), the Files API requires a [Hosted on Anthropic deployment](build-with-claude/claude-in-microsoft-foundry.md). [↩](#compat-fnref-1)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
