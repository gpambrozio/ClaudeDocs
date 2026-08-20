# Skills

Copy page



Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Each skill you add incurs a modest cost on the session's context window, adding instructions and metadata that help the model use the skill. Learn more in the [Agent Skills](agents-and-tools/agent-skills/overview.md) overview.

Skills reach your agent in two ways: attach them through the agent's `skills` array, or [load them from a GitHub repository](#load-skills-from-a-github-repository) mounted on the session. Attached skills come in two types. All skills work the same way: your agent invokes them automatically when they are relevant to the task.

- **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling (`pptx`, `xlsx`, `docx`, `pdf`).
- **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](agents-and-tools/agent-skills/overview.md) and [Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md). To upload a custom skill to your workspace, see [Create a custom skill](#create-a-custom-skill).

##  Create a custom skill

A custom skill is a directory containing a `SKILL.md` file plus any supporting files, uploaded to your workspace as a zip archive or as individual files. Creating the skill returns the `skill_*` ID you reference when attaching it to an agent. Anthropic pre-built skills are already available in every workspace and don't require this step. To use only pre-built skills, skip to [Attach skills to an agent](#attach-skills-to-an-agent).

The Skills API doesn't require a beta header. The cURL example still sends `anthropic-beta: skills-2025-10-02`, and the CLI and SDK `beta` commands add it automatically; requests that include it continue to work unchanged.

These examples omit the optional `display_title` field, so the skill's title is derived from `SKILL.md`. An explicitly passed `display_title` must be unique among the custom skills in your workspace.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:skills create \
  --file example_skill.zip
```

To list, retrieve, delete, and version custom skills, see [Managing custom skills](build-with-claude/skills-guide.md). For the full request and response schemas, see the [Create Skill API reference](api/beta/skills/create.md). Skill bundles upload directly to the Skills API rather than through the [Files API](build-with-claude/files.md).

##  Attach skills to an agent

Attach skills when creating an agent. Each [session](managed-agents/sessions.md) supports up to 500 skills, counted as the deduplicated set across every agent in the session (see [Multiagent orchestration](managed-agents/multiagent-orchestration.md)).

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
model: claude-opus-5
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
    version: latest
YAML
```

##  Load skills from a GitHub repository

Skills can also live in your codebase. When a session mounts a repository through the [`github_repository` resource](managed-agents/github.md), the repository's root `.claude/skills` directory is scanned at session start, and each skill found there becomes available to the agent. No upload and no entry in the agent's `skills` array are required. The agent sees each discovered skill's name, description, and path in the sandbox, and reads the skill's `SKILL.md` when a task matches, including any scripts and resources the skill ships. Discovery relies on the agent's `read` tool from the [agent toolset](managed-agents/tools.md), which is enabled by default; an agent with `read` disabled doesn't load repository skills.

Discovery finds skills at exactly `.claude/skills/<skill-name>/SKILL.md`, one directory level deep at the repository root:

- `your-repo/`
  - `.claude/`
    - `skills/`
      - `code-review/`
        - `SKILL.md`
      - `release-process/`
        - `SKILL.md`
        - `scripts/`
          - `run_checks.sh`
  - `src/`

Locations that don't match this layout aren't discovered at session start:

- `.claude/skills/SKILL.md`: a `SKILL.md` with no skill directory around it
- `.claude/skills/tools/code-review/SKILL.md`: nested more than one directory level deep
- `skills/code-review/SKILL.md`: a `skills` directory outside `.claude`

A `.claude/skills` directory elsewhere in the repository, such as inside a package subdirectory, isn't announced at session start; those skills can still surface when the agent reads files under that subtree.

Repository skills use the same `SKILL.md` format as the custom skills you upload. For the format and authoring guidance, see [Agent Skills](agents-and-tools/agent-skills/overview.md) and [Skill authoring best practices](agents-and-tools/agent-skills/best-practices.md).

To load skills from a repository, create a session that mounts it. This is the same request shown in [Accessing GitHub](managed-agents/github.md); `mount_path` is optional and defaults to `/workspace/<repo-name>`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
SESSION_ID=$(ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID" \
  --transform id --raw-output <<'EOF'
resources:
  - type: github_repository
    url: https://github.com/org/repo
    mount_path: /workspace/repo
    authorization_token: ghp_your_github_token
EOF
)
```

For private repositories, the resource's `authorization_token` must have access to the repository. This is the same personal access token flow used for any repository mount; see [Accessing GitHub](managed-agents/github.md).

Discovered skills follow the checked-out state of the repository: the `checkout` branch or commit when the resource sets one, otherwise the repository's default branch. The scan runs once, when the session starts. Commits pushed mid-session are not picked up; to load updated skills, start a new session.

Repository skills work alongside skills attached through the agent's `skills` array. If a repository skill shares a name with an attached skill, or with a skill from another mounted repository, both are available; each is announced with its own path.

##  Next steps



[Cloud environment setup](managed-agents/environments.md)

Customize cloud sandboxes for your sessions.



[Using Agent Skills with the API](build-with-claude/skills-guide.md)

Learn how to use Agent Skills to extend Claude's capabilities through the API.



[Files API](build-with-claude/files.md)

Upload files once and reference them across API requests.



[Get started with Agent Skills in the API](agents-and-tools/agent-skills/quickstart.md)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
