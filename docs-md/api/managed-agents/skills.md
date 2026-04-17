# Skills

Copy page

Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Unlike prompts (conversation-level instructions for one-off tasks), skills load on demand, only impacting the context window when needed.

Two types of skill are supported. Both work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling.
- **Custom skills:** Skills you author and upload to your organization.

To learn how to author custom skills, see the [Agent Skills overview](agents-and-tools/agent-skills/overview.md) and [best practices](agents-and-tools/agent-skills/best-practices.md). This page assumes you already have skills available in your organization or are using Anthropic pre-built skills.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Enable skills on a session

Attach skills when creating an agent. A maximum of 20 skills per session is supported - this includes skills across all agents for the session, if you are working with [multiple agents](managed-agents/multi-agent.md).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
agent = client.beta.agents.create(
    name="Financial Analyst",
    model="claude-opus-4-7",
    system="You are a financial analysis agent.",
    skills=[
        {
            "type": "anthropic",
            "skill_id": "xlsx",
        },
        {
            "type": "custom",
            "skill_id": "skill_abc123",
            "version": "latest",
        },
    ],
)
```

## Skill types

| Field | Description |
| --- | --- |
| `type` | Either `anthropic` for pre-built skills or `custom` for organization-authored skills. |
| `skill_id` | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation. |
| `version` | Custom skills only. Pin to a specific version or use `latest`. |

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
