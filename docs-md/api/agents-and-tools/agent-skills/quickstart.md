# Get started with Agent Skills in the API

Copy page



This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a request, and access the generated file.

##  Prerequisites

- A [Claude API key](/settings/keys) or a logged-in [ant CLI](cli-sdks-libraries/cli/authentication.md)
- A [client SDK](cli-sdks-libraries/overview.md) for your language, or `curl` and `jq`
- Basic familiarity with making API requests

##  Agent Skills overview

Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks such as creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:

- **PowerPoint (pptx):** Create and edit presentations
- **Excel (xlsx):** Create and analyze spreadsheets
- **Word (docx):** Create and edit documents
- **PDF (pdf):** Generate PDF documents

##  Step 1: List available Skills

First, check what Skills are available. Use the Skills API to list all Anthropic-managed Skills. Each language tab is an excerpt from one continuous script, with any imports and client setup at the top:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# List Anthropic-managed Skills
ant beta:skills list --source anthropic
```

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.

This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to determine which Skills are available. This is the first level of **progressive disclosure**, where Claude discovers Skills without loading their full instructions yet.

##  Step 2: Create a presentation

Use the PowerPoint Skill to create a presentation about renewable energy. Specify Skills using the `container` parameter in the Messages API:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# Create a message with the PowerPoint Skill
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    betas=["skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create a presentation about renewable energy with 5 slides",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)

print(f"stop_reason={response.stop_reason}, blocks={len(response.content)}")
```

The request includes the following parts:

- **`model`:** A [model that supports the code execution tool](agents-and-tools/tool-use/code-execution-tool.md)
- **`container.skills`:** Specifies which Skills Claude can use
- **`type: "anthropic"`:** Indicates this is an Anthropic-managed Skill
- **`skill_id: "pptx"`:** The PowerPoint Skill identifier
- **`version: "latest"`:** The Skill version set to the most recently published
- **`tools`:** Enables code execution (required for Skills)
- **Beta header:** `skills-2025-10-02`

When you make this request, Claude automatically matches your task to the relevant Skill. Because you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude runs the Skill's code to create your presentation.

##  Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The Step 2 `response` includes a file reference with a file ID. Extract the file ID and download the file with the Files API. The example saves it to your system temp directory:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# Extract the file ID. The code execution tool runs the Skill's code through
# its Bash sub-tool, and generated files appear as bash_code_execution_output
# items inside the bash_code_execution_tool_result block.
file_id = None
for block in response.content:
    if block.type == "bash_code_execution_tool_result":
        if block.content.type == "bash_code_execution_result":
            for output in block.content.content:
                file_id = output.file_id

if file_id:
    # Download the file and save it
    output_path = Path(tempfile.gettempdir()) / "renewable_energy.pptx"
    file_content = client.beta.files.download(file_id=file_id)
    file_content.write_to_file(output_path)
    print(f"Presentation saved to {output_path}")
```

##  Try more examples

Try these variations:

###  Create a spreadsheet

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    betas=["skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create a quarterly sales tracking spreadsheet with sample data",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

###  Create a Word document

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    betas=["skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "docx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Write a 2-page report on the benefits of renewable energy",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

###  Generate a PDF

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    betas=["skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pdf", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Generate a PDF invoice template",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

##  Next steps



[Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.



[Using Agent Skills with the API](build-with-claude/skills-guide.md)

Learn how to use Agent Skills to extend Claude's capabilities through the API.



[Create custom Skills](api/skills/create-skill.md)

Upload your own Skills for specialized tasks.



[Use Skills in Claude Code](skills.md)



Learn about Skills in Claude Code.



[Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)



Explore example Skills and implementation patterns.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
