# Skills

Copy page



Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Each skill you add incurs a modest cost on the session's context window, adding instructions and metadata that help the model use the skill. Learn more in the [Agent Skills](agents-and-tools/agent-skills/overview.md) overview.

You can attach two types of skill. Both work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling (`pptx`, `xlsx`, `docx`, `pdf`).
- **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](agents-and-tools/agent-skills/overview.md) and [Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md). To upload a custom skill to your workspace, see [Create a custom skill](#create-a-custom-skill).



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](api/beta-headers.md).

##  Create a custom skill

A custom skill is a directory containing a `SKILL.md` file plus any supporting files, uploaded to your workspace as a zip archive or as individual files. Creating the skill returns the `skill_*` ID you reference when attaching it to an agent. Anthropic pre-built skills are already available in every workspace and don't require this step. To use only pre-built skills, skip to [Attach skills to an agent](#attach-skills-to-an-agent).

When you call the Skills API directly with cURL, pass the `anthropic-beta: skills-2025-10-02` header explicitly. The CLI and SDKs send it automatically.

These examples omit the optional `display_title` field, so the skill's title is derived from `SKILL.md`. An explicitly passed `display_title` must be unique among the custom skills in your workspace.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:skills create \
  --file example_skill.zip
```

To list, retrieve, delete, and version custom skills, see [Managing custom skills](build-with-claude/skills-guide.md). For the full request and response schemas, see the [Create Skill API reference](api/beta/skills/create.md). Skill bundles upload directly to the Skills API rather than through the [Files API](build-with-claude/files.md).

##  Attach skills to an agent

Attach skills when creating an agent. Each [session](managed-agents/sessions.md) supports up to 500 skills total, counted across every agent in the session (see [Multiagent orchestration](managed-agents/multiagent-orchestration.md)).



Mounting more skills increases the time it takes for the session's sandbox to start. Attach only the skills each agent needs for its task.

Each entry in the `skills` array uses the following fields:

| Field | Description |
| --- | --- |
| `type` | Either `anthropic` for pre-built skills or `custom` for workspace-authored skills. |
| `skill_id` | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation (see [Create a custom skill](#create-a-custom-skill)). |
| `version` | Pin to a specific version or use `latest`. Optional. Defaults to `latest` when omitted. Applies to both Anthropic and custom skills. |

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents create <<'YAML'
name: Financial Analyst
model: claude-opus-4-8
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_abc123
    version: latest
YAML
```

##  Next steps

[

Cloud environment setup

Customize cloud sandboxes for your sessions.](managed-agents/environments.md)[

Using Agent Skills with the API

Learn how to use Agent Skills to extend Claude's capabilities through the API.](build-with-claude/skills-guide.md)[

Files API

Upload files once and reference them across API requests.](build-with-claude/files.md)[

Get started with Agent Skills in the API

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.](agents-and-tools/agent-skills/quickstart.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
