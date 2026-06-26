# Files API

Copy page



The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md) to provide inputs (e.g. datasets and documents) and then download outputs (e.g. charts). You can also use the Files API to prevent having to continually re-upload frequently used documents and images across multiple API calls. You can [explore the API reference directly](api/files-create.md), in addition to this guide.



The Files API is in beta. Reach out through the [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.



This feature is **not** eligible for [Zero Data Retention (ZDR)](build-with-claude/api-and-data-retention.md). Data is retained according to the feature's standard retention policy.

##  Supported models

Referencing a `file_id` in a Messages request is supported on all models that support the given file type. [Images](build-with-claude/vision.md) are supported on all current Claude models. For [PDFs](build-with-claude/pdf-support.md) and [other file types with the code execution tool](agents-and-tools/tool-use/code-execution-tool.md), see the linked pages for model support.

The Files API is available on the Claude API, [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), and [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md). It is not currently available on Amazon Bedrock or Google Cloud.

##  How the Files API works

The Files API provides a simple create-once, use-many-times approach for working with files:

- **Upload files** to Anthropic's secure storage and receive a unique `file_id`
- **Download files** that are created from skills or the code execution tool
- **Reference files** in [Messages](api/messages/create.md) requests using the `file_id` instead of re-uploading content
- **Manage your files** with list, retrieve, and delete operations

##  How to use the Files API



To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

###  Uploading a file

Upload a file to be referenced in future API calls:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
uploaded = client.beta.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
)
```

The response from uploading a file will include:

Output

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

###  Using a file in messages

Once uploaded, reference the file using its `file_id`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.beta.messages.create(
    model="claude-opus-4-8",
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

| File Type | MIME Type | Content Block Type | Use Case |
| --- | --- | --- | --- |
| PDF | `application/pdf` | `document` | Text analysis, document processing |
| Plain text | `text/plain` | `document` | Text analysis, processing |
| Images | `image/jpeg`, `image/png`, `image/gif`, `image/webp` | `image` | Image analysis, visual tasks |
| [Datasets, others](agents-and-tools/tool-use/code-execution-tool.md) | Varies | `container_upload` | Analyze data, create visualizations |

###  Working with other file formats

For file types that are not supported as `document` blocks (.csv, .txt, .md, .docx, .xlsx), convert the files to plain text, and include the content directly in your message:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import pandas as pd
# ...
# Example: Reading a CSV file
df = pd.read_csv("data.csv")
csv_content = df.to_string()

# Send as plain text in the message
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Here's the CSV data:\n\n{csv_content}\n\nPlease analyze this data.",
                }
            ],
        }
    ],
)

print(response.content[0].text)
```



For .docx files containing images, convert them to PDF format first, then use [PDF support](build-with-claude/pdf-support.md) to take advantage of the built-in image parsing. This allows using citations from the PDF document.

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

###  Managing files

####  List files

Retrieve a list of your uploaded files:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
files = client.beta.files.list()
```

####  Get file metadata

Retrieve information about a specific file:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file = client.beta.files.retrieve_metadata(file_id)
```

####  Delete a file

Remove a file from your workspace:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
result = client.beta.files.delete(file_id)
```

###  Downloading a file

Download files that have been created by skills or the code execution tool:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file_content = client.beta.files.download(file_id)

# Save to file
file_content.write_to_file("downloaded_file.txt")
```



You can only download files that were created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md). Files that you uploaded cannot be downloaded.

---

##  File storage and limits

###  Storage limits

- **Maximum file size:** 500 MB per file
- **Total storage:** 500 GB per organization

###  File lifecycle

- Files are scoped to the workspace of the API key. Other API keys can use files created by any other API key associated with the same workspace
- Files persist until you delete them
- Deleted files cannot be recovered
- Files are inaccessible via the API shortly after deletion, but they may persist in active `Messages` API calls and associated tool uses
- Files that users delete will be deleted in accordance with Anthropic's [data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).

---

##  Data retention

Files uploaded via the Files API are retained until explicitly deleted using the `DELETE /v1/files/{file_id}` endpoint. Files are stored for reuse across multiple API requests.

For ZDR eligibility across all features, see [API and data retention](manage-claude/api-and-data-retention.md).

##  Error handling

Common errors when using the Files API include:

- **File not found (404):** The specified `file_id` doesn't exist or you don't have access to it
- **Invalid file type (400):** The file type doesn't match the content block type (e.g., using an image file in a document block)
- **Exceeds context window size (400):** The file is larger than the context window size (e.g. using a 500 MB plaintext file in a `/v1/messages` request)
- **Invalid filename (400):** Filename doesn't meet the length requirements (1-255 characters) or contains forbidden characters (`<`, `>`, `:`, `"`, `|`, `?`, `*`, `\`, `/`, or unicode characters 0-31)
- **File too large (413):** File exceeds the 500 MB limit
- **Storage limit exceeded (403):** Your organization has reached the 500 GB storage limit

Output



```shiki
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "File not found: file_011CNha8iCJcU1wXNR6q4V8w"
  }
}
```

##  Usage and billing

File API operations are **free**:

- Uploading files
- Downloading files
- Listing files
- Getting file metadata
- Deleting files

File content used in `Messages` requests are priced as input tokens. You can only download files created by [skills](build-with-claude/skills-guide.md) or the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md).

###  Rate limits

During the beta period:

- File-related API calls are limited to approximately 100 requests per minute
- [Contact us](/cdn-cgi/l/email-protection#86f5e7eae3f5c6e7e8f2eef4e9f6efe5a8e5e9eb) if you need higher limits for your use case

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
