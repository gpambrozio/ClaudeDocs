# Accessing GitHub

Copy page



You can mount a GitHub repository to your session sandbox and connect to the GitHub MCP for making pull requests.

GitHub repositories are cached, so future sessions that use the same repository start faster.

## GitHub MCP and session resources

First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no authentication token:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
AGENT_ID=$(ant beta:agents create --transform id --raw-output < code-reviewer.agent.yaml)
```

code-reviewer.agent.yaml



```shiki
name: Code Reviewer
model:
  id: claude-opus-5
system: You are a code review assistant with access to GitHub.
mcp_servers:
  - type: url
    name: github
    url: https://api.githubcopilot.com/mcp/
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
```

Then create a session that mounts the GitHub repository:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
        },
    ],
)
```

A `github_repository` resource accepts the following fields:

| Field | Description |
| --- | --- |
| `type` | Required. Must be `"github_repository"`. |
| `url` | Required. The repository's HTTPS URL in the form `https://github.com/<owner>/<repo>`, without a `.git` suffix. Other forms, including SSH URLs, are rejected with an `invalid_request_error`. |
| `authorization_token` | Required. The GitHub token used to clone the repository. It is not echoed in API responses. See [Token permissions](#token-permissions). |
| `mount_path` | Optional. The directory under `/workspace` to clone the repository into. Defaults to `/workspace/<repo-name>`. |
| `checkout` | Optional. A branch (`{"type": "branch", "name": "main"}`) or commit (`{"type": "commit", "sha": "..."}`) to check out. Defaults to the repository's default branch. |

Mounting a repository also loads any skills stored in its root `.claude/skills` directory. Skills are discovered once per session, from the repository state checked out at session start. See [Load skills from a GitHub repository](managed-agents/skills.md).

## Token permissions

When providing a GitHub token, use the minimum required permissions:

| Action | Required scopes |
| --- | --- |
| Clone private repos | `repo` |
| Create PRs | `repo` |
| Read issues | `repo` (private) or `public_repo` |
| Create issues | `repo` (private) or `public_repo` |

## Multiple repositories

Mount multiple repositories by adding entries to the `resources` array:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
resources = [
    {
        "type": "github_repository",
        "url": "https://github.com/org/frontend",
        "mount_path": "/workspace/frontend",
        "authorization_token": "ghp_your_github_token",
    },
    {
        "type": "github_repository",
        "url": "https://github.com/org/backend",
        "mount_path": "/workspace/backend",
        "authorization_token": "ghp_your_github_token",
    },
]
```

## Managing repositories on a running session

After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or through `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data[0].id
print(repo_resource_id)  # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
    repo_resource_id,
    session_id=session.id,
    authorization_token="ghp_your_new_github_token",
)
```

## Creating pull requests

With the GitHub MCP server, the agent can create branches, commit changes, and push them:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
                },
            ],
        },
    ],
)
```

## Next steps



[Session event stream](managed-agents/events-and-streaming.md)

Stream events and steer the agent while it opens the pull request



[MCP connector](managed-agents/mcp-connector.md)

Connect more MCP servers to give the agent additional tools



[Adding files](managed-agents/files.md)

Mount files in the sandbox alongside your repositories

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
