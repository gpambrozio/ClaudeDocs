# Using Agent Skills with the API

Copy page



Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.

##  Quick links

[Get started with Agent Skills in the API](agents-and-tools/agent-skills/quickstart.md)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.



[Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.

##  Overview

Skills integrate with the Messages API through the [code execution tool](agents-and-tools/tool-use/code-execution-tool.md). Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.

###  Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they run in the code execution environment.

You can use Skills from two sources:

| Aspect | Anthropic Skills | Custom Skills |
| --- | --- | --- |
| **Type value** | `anthropic` | `custom` |
| **Skill IDs** | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv` |
| **Version format** | Date-based: `20251013` or `latest` | Version ID: `skver_01AbCdEfGhIjKlMnOpQrStUv` or `latest` |
| **Management** | Pre-built and maintained by Anthropic | Upload and manage through the [Skills API](api/beta/skills/create.md) |
| **Availability** | Available to all users | Private to your workspace |

Both skill sources are returned by the [List Skills endpoint](api/beta/skills/list.md) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.

###  Prerequisites

To use Skills, you need:

1. **Claude API key** from the [Claude Console](/settings/keys)
2. **[Code execution tool](agents-and-tools/tool-use/code-execution-tool.md)** enabled in your requests

Skills are generally available on the Claude API and don't require an `anthropic-beta` header, either for the Skills API or for `container.skills` in Messages requests. The examples in this guide still send the `skills-2025-10-02` beta header (plus `code-execution-2025-08-25` in Messages requests) and use the SDKs' `beta` namespace. Both headers remain valid opt-ins, so the examples work as written, and you can omit them in your own requests.

Skills require the code execution tool, so use a model from its [model compatibility list](agents-and-tools/tool-use/code-execution-tool.md).

---

##  Using Skills in Messages

###  Container parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 20 Skills for each request.

The structure is identical for both Anthropic and custom Skills. Specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

###  Downloading generated files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1. Skills create files during code execution.
2. The response includes a `file_id` for each created file, inside code-execution tool result blocks (see [Response format](agents-and-tools/tool-use/code-execution-tool.md)).
3. Use the Files API to download the actual file content.
4. Save locally or process as needed.

To provide input files for Skills to work on, [upload them with the Files API](build-with-claude/files.md) and reference them in your request with a [container upload block](build-with-claude/files.md).

**Example: creating and downloading an Excel file**

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create an Excel file with a simple budget spreadsheet",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Step 2: Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == "bash_code_execution_tool_result":
            content_item = item.content
            if content_item.type == "bash_code_execution_result":
                # each content item is a bash_code_execution_output block carrying a file_id
                for file in content_item.content:
                    file_ids.append(file.file_id)
    return file_ids

# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id=file_id)
    file_content = client.beta.files.download(file_id=file_id)

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

**Additional Files API operations:**

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()
file_id = "file_011CNha8iCJcU1wXNR6q4V8w"
# Get file metadata
file_info = client.beta.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
for file in client.beta.files.list():
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id=file_id)
```

###  Multi-turn conversations

The response's `container` object carries the container's `id` and `expires_at` timestamp (see [Container reuse](agents-and-tools/tool-use/code-execution-tool.md) for lifetime details). Reuse the same container across multiple messages by specifying the container ID:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# First request creates container
response1 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a sample sales dataset and analyze it"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Create a sample sales dataset and analyze it"},
    {
        # Carry the assistant's text forward; container.id carries the execution state
        "role": "assistant",
        "content": "\n".join(
            block.text for block in response1.content if block.type == "text"
        ),
    },
    {"role": "user", "content": "What was the total revenue?"},
]

response2 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

###  Long-running operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

messages = [{"role": "user", "content": "Generate and process a large sample dataset"}]
max_retries = 10

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            }
        ]
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Handle pause_turn for long operations
for _ in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.beta.messages.create(
        model="claude-opus-5",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "id": response.container.id,
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ],
        },
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
```

###  Using multiple Skills

Combine multiple Skills in a single request to handle complex workflows:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            },
        ]
    },
    messages=[
        {"role": "user", "content": "Analyze sales data and create a presentation"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

---

##  Managing custom Skills

###  Creating a Skill

A Skill bundle is a directory containing a `SKILL.md` file at the top level with `name` and `description` YAML frontmatter, plus any supporting scripts or resources. See [Get started with Agent Skills in the API](agents-and-tools/agent-skills/quickstart.md) to author one, and the **Requirements** list following the examples for the full constraints.

Upload your custom Skill to make it available in your workspace. You can upload a zip archive or individual file objects. The Python SDK also provides a `files_from_dir` helper that accepts a directory path.

Files are identified by the filename you attach (the `;filename=` suffix in the cURL example and the filename arguments in the SDK examples). For the walkthrough's skill, create a zip with `zip -r financial_skill.zip financial_skill/` and substitute it for the `example_skill.zip` placeholder in the zip-upload options.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:skills create \
  --file example_skill.zip \
  --beta skills-2025-10-02

# Per-file upload requires path-qualified filenames, which the CLI
# can't currently set. Upload a zip archive instead.
```

**Requirements:**

- Must include a `SKILL.md` file at the upload root (or at the top of a single enclosing folder)
- `display_name` is optional: when omitted, it derives from the `SKILL.md` `name`; an explicit value may be up to 255 characters and does not need to be unique within the workspace
- Total upload size must be under 30 MB (uncompressed)
- YAML frontmatter requirements:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](api/beta/skills/create.md).

###  Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# List all Skills
ant beta:skills list

# List only custom Skills
ant beta:skills list --source custom
```

See the [List Skills API reference](api/beta/skills/list.md) for pagination and filtering options.

###  Retrieving a Skill

Get details about a specific Skill:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:skills retrieve \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv
```

###  Deleting a Skill

Deleting a Skill also removes all of its versions. The cascade is GA-only behavior, so unlike the other examples in this guide, these call the GA surface directly rather than the `beta` namespace.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant skills delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv >/dev/null
```

###  Versioning

Skills support versioning to manage updates safely:

**Anthropic Skills:**

- Versions use date format: `20251013`
- New versions released as updates are made
- Specify exact versions for stability

**Custom Skills:**

- Auto-generated version IDs: `skver_01AbCdEfGhIjKlMnOpQrStUv`
- Use `"latest"` to always get the most recent version
- Create new versions when updating Skill files

A new version is a complete snapshot, not a delta: upload the Skill's full file set each time. Files you omit are not carried over, and the `name` in the new version's `SKILL.md` must match the Skill's existing name. The following examples re-upload the complete `financial_skill/` bundle from [Creating a Skill](#creating-a-skill).

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# Create a new version
VERSION_NUMBER=$(ant beta:skills:versions create \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --file financial_skill.zip \
  --transform version \
  --raw-output)

# Use specific version
ant beta:messages create \
  --beta code-execution-2025-08-25,skills-2025-10-02 <<YAML
model: claude-opus-5
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: "$VERSION_NUMBER"
messages:
  - role: user
    content: Use updated Skill
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Use latest version
ant beta:messages create \
  --beta code-execution-2025-08-25,skills-2025-10-02 <<YAML
model: claude-opus-5
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Use latest Skill version
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

See the [Create Skill Version API reference](api/beta/skills/versions/create.md) for complete details.

---

##  How Skills are loaded

When you specify Skills in a container:

1. **Metadata discovery:** Claude sees metadata for each Skill (name, description) in the system prompt.
2. **File loading:** Skill files are copied into the container at `/skills/{skill-name}/`. The directory is the Skill's name (`pptx` for an Anthropic Skill, the `SKILL.md` `name` for a custom Skill), not its `skill_01...` ID.
3. **Automatic use:** Claude automatically loads and uses Skills when relevant to your request.
4. **Composition:** Multiple Skills compose together for complex workflows.

Claude loads full Skill instructions only when needed.

---

##  Use cases

Skills fit both organizational and personal work. Organizations use them to apply brand formatting to documents, structure notes and reports around company templates, and run company-specific analytical procedures. Individuals use them for custom document templates, specialized data pipelines, and code generation or deployment conventions.

###  Example: financial modeling

Combine Excel and custom DCF analysis Skills:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
from anthropic.lib import files_from_dir

client = anthropic.Anthropic()

# Create custom DCF analysis Skill

dcf_skill = client.beta.skills.create(
    files=files_from_dir("/path/to/dcf_skill"),
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"},
        ]
    },
    messages=[
        {
            "role": "user",
            "content": "Build a DCF valuation model for a SaaS company",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
print(response)
```

---

##  Limits and constraints

###  Request limits

- **Maximum Skills per request:** 20
- **Maximum Skill upload size:** 30 MB (all files combined, uncompressed)
- **YAML frontmatter requirements:**
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

###  Environment constraints

Skills run in the code execution container with these limitations:

- **No network access:** Cannot make external API calls
- **No runtime package installation:** Only pre-installed packages available
- **Isolated environment:** A fresh container is created unless you specify an existing container ID

See [Code execution tool](agents-and-tools/tool-use/code-execution-tool.md) for available packages.

---

##  Best practices

###  When to use multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**

- Data analysis (Excel) + presentation creation (PowerPoint)
- Report generation (Word) + export to PDF
- Custom domain logic + document generation

**Avoid:**

- Including unused Skills (impacts performance)

###  Version management strategy

The SDK tabs in this section show the `container` value to include in a Messages request. The cURL and CLI tabs show the full request.

**For production:** pin a specific version, so Skill updates never change your deployed behavior. If you omit `version` or set it to `"latest"`, requests use the newest version of the Skill, so a version uploaded by anyone in the [workspace](#workspace-scoped-access) immediately changes what your production agents run. The version ID comes from the create-version response in [Versioning](#versioning) or from the [List Skill Versions API](api/beta/skills/versions/list.md). The ID is always a string: quote epoch-timestamp IDs in JSON or YAML.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# Pin to specific versions for stability
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "1759178010641129",
        }
    ]
}
```

**For development:** use `latest` to pick up the newest version automatically as you iterate.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# Use latest for active development
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",
        }
    ]
}
```

###  Prompt caching considerations

If you use [Prompt caching](build-with-claude/prompt-caching.md), changing the Skills list in your container breaks the cache. Skills render into the system prompt in a fixed order, so the same list produces the same cacheable prefix:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

# Skills render into the system prompt in a fixed, cache-friendly order
response1 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
    ],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Changing the Skills list ([xlsx] vs [xlsx, pptx]) changes the prefix: a cache miss, while an identical list is a cache hit
response2 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
    ],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # prefix change: cache miss
        ]
    },
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

For best caching performance, keep your Skills list, including its order, consistent across requests. Pinning custom Skill versions also helps: with `"latest"`, publishing a new version can invalidate the cached prefix if it changes the Skill's description.

###  Error handling

Handle Skill-related errors gracefully:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

try:
    response = client.beta.messages.create(
        model="claude-opus-5",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ]
        },
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise
```

---

##  Data retention

Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](manage-claude/api-and-data-retention.md).

##  Audit logging

If your organization has the [Compliance API](manage-claude/compliance-api.md) enabled, its [Activity Feed](manage-claude/compliance-activity-feed.md) records the creation and deletion of Skills and Skill versions made with a Claude API key or from the Claude Console. Operations that occur while the Compliance API is off are not recorded and cannot be recovered later, so [set up the Compliance API](manage-claude/compliance-api-access.md) before you rely on this audit trail.

##  Next steps



[API reference](api/beta/skills/create.md)

Complete API reference with all endpoints



[Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.



[Code execution tool](agents-and-tools/tool-use/code-execution-tool.md)

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
