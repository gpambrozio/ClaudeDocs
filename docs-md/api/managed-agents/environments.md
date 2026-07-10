# Cloud environment setup

Copy page



Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).

This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](managed-agents/self-hosted-sandboxes.md).



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](api/beta-headers.md).

##  Create an environment

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create \
  --name "python-dev" \
  --config '{type: cloud, networking: {type: unrestricted}}'
```

Use a unique, descriptive `name` so you can tell environments apart.

##  Use the environment in a session

Pass the environment ID as a string when [creating a session](managed-agents/sessions.md).

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"
```

##  Configuration options

###  Packages

The `packages` field pre-installs packages into the sandbox before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions. Unpinned packages install the latest version.

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create <<'YAML'
name: data-analysis
config:
  type: cloud
  packages:
    pip:
      - pandas
      - numpy
      - scikit-learn
    npm:
      - express
  networking:
    type: unrestricted
YAML
```

Supported package managers:

| Field | Package manager | Example |
| --- | --- | --- |
| `apt` | System packages (apt-get) | `"ffmpeg"` |
| `cargo` | Rust (cargo) | `"ripgrep@14.0.0"` |
| `gem` | Ruby (gem) | `"rails:7.1.0"` |
| `go` | Go modules | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm` | Node.js (npm) | `"express@4.18.0"` |
| `pip` | Python (pip) | `"pandas==2.2.0"` |

###  Networking

The `networking` field controls the sandbox's outbound network access. It does not affect the allowed domains for the `web_search` or `web_fetch` tools.

| Mode | Description |
| --- | --- |
| `unrestricted` | Full outbound network access, except for a general safety blocklist. This is the default. |
| `limited` | Restricts sandbox network access to the hosts in `allowed_hosts`. Set `allow_package_managers` and `allow_mcp_servers` to `true` to allow additional access. |

The following example creates an environment with `limited` networking:

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create <<'YAML'
name: api-access
config:
  type: cloud
  networking:
    type: limited
    allowed_hosts:
      - api.example.com
    allow_mcp_servers: true
    allow_package_managers: true
YAML
```



For production deployments, use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed domains.

When using `limited` networking:

- `allowed_hosts` specifies domains the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`). Do not include a URL scheme, port, or path.
- `allow_mcp_servers` allows outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
- `allow_package_managers` allows outbound access to public package registries (such as PyPI and npm) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

##  Environment lifecycle

- Environments persist until explicitly archived or deleted.
- Each session gets its own sandbox instance, even when multiple sessions reference the same environment. Sessions do not share filesystem state.
- Environments are not versioned. If you update an environment frequently, keep your own record of the changes so you can tell which configuration each session used.

##  Manage environments

curlCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# List environments
ant beta:environments list

# Retrieve a specific environment
ant beta:environments retrieve --environment-id "$ENVIRONMENT_ID"

# Archive an environment (read-only, existing sessions continue)
ant beta:environments archive --environment-id "$ENVIRONMENT_ID"

# Delete an environment (only if no sessions reference it)
ant beta:environments delete --environment-id "$ENVIRONMENT_ID"
```

##  Pre-installed runtimes

Cloud sandboxes include common runtimes out of the box. See [Cloud sandbox reference](managed-agents/cloud-sandboxes-reference.md) for the full list of pre-installed languages, databases, and utilities.

##  Next steps

[

Cloud sandbox reference

Pre-installed packages, databases, and utilities available in cloud sandboxes.](managed-agents/cloud-sandboxes-reference.md)[

Start a session

Create a session to run your agent and start running tasks.](managed-agents/sessions.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
