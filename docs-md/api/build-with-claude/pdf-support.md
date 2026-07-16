# PDF support

Copy page





This feature is eligible for [Zero Data Retention (ZDR)](build-with-claude/api-and-data-retention.md). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

You can ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

- Analyzing financial reports and understanding charts/tables
- Extracting key information from legal documents
- Translation assistance for documents
- Converting document information into structured formats

##  Before you begin

###  Check PDF requirements

Claude works with any standard PDF. Ensure your request size meets these requirements:

| Requirement | Limit |
| --- | --- |
| Maximum request size | 32 MB ([varies by platform](api/overview.md)) |
| Maximum pages per request | 600 (100 when the request's context window is under 1M tokens) |
| Format | Standard PDF (no passwords/encryption) |

Both limits are on the entire request payload, including any other content sent alongside PDFs. For large PDFs, consider uploading with the [Files API](#option-3-files-api) and referencing by `file_id` to keep request payloads small.



Dense PDFs (many small-font pages, complex tables, or heavy graphics) can fill the context window before reaching the page limit. Requests with large PDFs can also fail before reaching the page limit, even when using the Files API. Try splitting the document into sections; for large files, because each page is processed as an image, downsampling embedded images can also help.

Because PDF support relies on Claude's vision capabilities, it is subject to the same [limitations and considerations](build-with-claude/vision.md) as other vision tasks.

###  Supported platforms and models

PDF support is available on the Claude API, [Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md) (see [Amazon Bedrock PDF support](#amazon-bedrock-pdf-support)), [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), [Google Cloud](build-with-claude/claude-on-vertex-ai.md), and [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md). All [active models](about-claude/models/overview.md) support PDF processing.

###  Amazon Bedrock PDF support

When using PDF support through the Converse API, part of [Claude on Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude/claude-on-amazon-bedrock-legacy.md), there are two distinct document processing modes:



**Important:** To access Claude's full visual PDF understanding capabilities in the Converse API, you must enable citations. Without citations enabled, the API falls back to basic text extraction only. Learn more about [working with citations](build-with-claude/citations.md).

####  Document processing modes

1. **Converse Document Chat** (Original mode - Text extraction only)

   - Provides basic text extraction from PDFs
   - Cannot analyze images, charts, or visual layouts within PDFs
   - Uses approximately 1,000 tokens for a 3-page PDF
   - Automatically used when citations are not enabled
2. **Claude PDF Chat** (New mode - Full visual understanding)

   - Provides complete visual analysis of PDFs
   - Can understand and analyze charts, graphs, images, and visual layouts
   - Processes each page as both text and image for comprehensive understanding
   - Uses approximately 7,000 tokens for a 3-page PDF
   - **Requires citations to be enabled** in the Converse API

####  Key limitations

- **Converse API**: Visual PDF analysis requires citations to be enabled. There is currently no option to use visual analysis without citations (unlike the InvokeModel API).
- **InvokeModel API**: Provides full control over PDF processing without forced citations.

####  Common issues

If Claude isn't seeing images or charts in your PDFs when using the Converse API, you likely need to enable the citations flag. Without it, Converse falls back to basic text extraction only.



This is a known constraint with the Converse API. For applications that require visual PDF analysis without citations, consider using the InvokeModel API instead.



Plain text files such as .txt, .csv, or .md can be used directly in document blocks: upload them to the Files API with MIME type `text/plain` and reference them by `file_id`. Binary formats such as .xlsx or .docx are not supported in document blocks and must be converted to text or PDF first. See [Working with other file formats](build-with-claude/files.md).

##  Process PDFs with Claude

###  Send your first PDF request

Start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:

1. As a URL reference to a PDF hosted online
2. As a base64-encoded PDF in `document` content blocks
3. By a `file_id` from the [Files API](build-with-claude/files.md)



On Amazon Bedrock and Google Cloud, only base64-encoded sources are currently available. On Microsoft Foundry, the Files API is not supported for deployments hosted on Azure.

####  Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "url",
                        "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf",
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

The response returns Claude's analysis as text blocks in `content`, with token consumption in `usage`:

Output



```shiki
{
  "id": "msg_01Hfp8YuFjQ55VgWbpdHDehB",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-4-8",
  "content": [
    {
      "type": "text",
      "text": "This document is an addendum to the Claude 3 model card, reporting updated evaluation results. The key findings include..."
    }
  ],
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 45000,
    "output_tokens": 300
  }
}
```

####  Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn't available:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import httpx

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Alternative: Load from a local file
# with open("document.pdf", "rb") as f:
#     pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

# Send to Claude using base64 encoding
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

####  Option 3: Files API

For PDFs you'll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](build-with-claude/files.md) (beta):

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# Upload the PDF file
with open("/path/to/document.pdf", "rb") as f:
    file_upload = client.beta.files.upload(file=("document.pdf", f, "application/pdf"))

# Use the uploaded file in a message
message = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "What are the key findings in this document?"},
            ],
        }
    ],
)

print(message.content)
```

###  How PDF support works

When you send a PDF to Claude, the following steps occur:

1. 1

   The system extracts the contents of the document.

   - The system converts each page of the document into an image.
   - The text from each page is extracted and provided alongside each page's image.
2. 2

   Claude analyzes both the text and images to better understand the document.

   - Documents are provided as a combination of text and images for analysis.
   - This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.
3. 3

   Claude responds, referencing the PDF's contents if relevant.

   Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

   - [Prompt caching](#use-prompt-caching): To improve performance for repeated analysis.
   - [Batch processing](#process-document-batches): For high-volume document processing.
   - [Tool use](agents-and-tools/tool-use/overview.md): To extract specific information from documents for use as tool inputs.

###  Estimate your costs

The token count of a PDF file depends on the total text extracted from the document and the number of pages:

- Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
- Image token costs: Because each page is converted into an image, the same [image-based cost calculations](build-with-claude/vision.md) are applied.

You can use [token counting](build-with-claude/token-counting.md) to estimate costs for your specific PDFs.

##  Optimize PDF processing

###  Improve performance

Follow these best practices for optimal results:

- Place PDFs before text in your requests
- Use standard fonts
- Ensure text is clear and legible
- Rotate pages to proper upright orientation
- Use logical page numbers (from PDF viewer) in prompts
- Split large PDFs into chunks when needed
- Enable prompt caching for repeated analysis

###  Scale your implementation

For high-volume processing, consider these approaches:

####  Use prompt caching

Cache PDFs with [prompt caching](build-with-claude/prompt-caching.md) to improve performance on repeated queries:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import httpx

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Create a message with the cached document
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data,
                    },
                    "cache_control": {"type": "ephemeral"},
                },
                {
                    "type": "text",
                    "text": "Which model has the highest human preference win rates across each use-case?",
                },
            ],
        }
    ],
)

print(message.content)
```

####  Process document batches

Use the [Message Batches API](build-with-claude/batch-processing.md) to process many PDFs in one request:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
import base64
import httpx

# First, load and encode the PDF
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(
    httpx.get(pdf_url, follow_redirects=True).content
).decode("utf-8")

# Create a batch of requests that use the document
client = anthropic.Anthropic()
message_batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": "Which model has the highest human preference win rates across each use-case?",
                            },
                        ],
                    }
                ],
            },
        },
        {
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": "Extract 5 key insights from this document.",
                            },
                        ],
                    }
                ],
            },
        },
    ]
)

print(message_batch)
```

Batches process asynchronously. To check progress and retrieve results once processing ends, see [Batch processing](build-with-claude/batch-processing.md).

##  Next steps

[

Vision

Claude's vision capabilities allow it to understand and analyze images, opening up exciting possibilities for multimodal interaction.](build-with-claude/vision.md)[

Try PDF examples



Explore practical examples of PDF processing in the cookbook recipe.](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision)[

View API reference

See complete API documentation for PDF support.](api/messages/create.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
