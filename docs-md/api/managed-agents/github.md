# Accessing GitHub

Copy page

You can mount a GitHub repository to your session container and connect to the GitHub MCP for making pull requests.

GitHub repositories are cached, so future sessions that use the same repository start faster.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## GitHub MCP and Session Resources

First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no auth token:

CLI

```shiki
AGENT_ID=$(ant beta:agents create \
  --name "Code Reviewer" \
  --model '{id: claude-sonnet-4-6}' \
  --system "You are a code review assistant with access to GitHub." \
  --mcp-server '{type: url, name: github, url: https://api.githubcopilot.com/mcp/}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --format yaml)
```

Then create a session that mounts the GitHub repository:

curl

```shiki
session_id=$(curl -fsS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<JSON | jq -r '.id'
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "resources": [
    {
      "type": "github_repository",
      "url": "https://github.com/org/repo",
      "mount_path": "/workspace/repo",
      "authorization_token": "ghp_your_github_token"
    }
  ]
}
JSON
)
```

The `resources[].authorization_token` authenticates the repository clone operation and is not echoed in API responses.

## Token permissions

When providing a GitHub token, use the minimum required permissions:

| Action | Required scopes |
| --- | --- |
| Clone private repos | `repo` |
| Create PRs | `repo` |
| Read issues | `repo` (private) or `public_repo` |
| Create issues | `repo` (private) or `public_repo` |

Use fine-grained personal access tokens with minimum required permissions. Avoid using tokens with broad access to your GitHub account.

## Multiple repositories

Mount multiple repositories by adding entries to the `resources` array:

curl

```shiki
resources='[
  {
    "type": "github_repository",
    "url": "https://github.com/org/frontend",
    "mount_path": "/workspace/frontend",
    "authorization_token": "ghp_your_github_token"
  },
  {
    "type": "github_repository",
    "url": "https://github.com/org/backend",
    "mount_path": "/workspace/backend",
    "authorization_token": "ghp_your_github_token"
  }
]'
```

## Managing repositories on a running session

After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or via `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.

curl

```shiki
# List resources on the session
repo_resource_id=$(curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/resources" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" | jq -r '.data[0].id')
echo "$repo_resource_id"  # "sesrsc_01ABC..."

# Rotate the authorization token
curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/resources/$repo_resource_id" \
# ...
  -o /dev/null \
  --data @- <<JSON
{
  "authorization_token": "ghp_your_new_github_token"
}
JSON
```

## Creating pull requests

With the GitHub MCP server, the agent can create branches, commit changes, and push them:

curl

```shiki
curl -fsS "https://api.anthropic.com/v1/sessions/$session_id/events" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -o /dev/null \
  --data @- <<JSON
{
  "events": [
    {
      "type": "user.message",
      "content": [
        {
          "type": "text",
          "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it."
        }
      ]
    }
  ]
}
JSON
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
