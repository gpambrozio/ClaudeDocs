# Cloud environment setup

Copy page



Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).

This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](managed-agents/self-hosted-sandboxes.md).

##  Create an environment

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create < python-dev.environment.yaml
```

python-dev.environment.yaml



```shiki
name: python-dev
config:
  type: cloud
  networking:
    type: unrestricted
```

Use a unique, descriptive `name` so you can tell environments apart.

##  Use the environment in a session

Pass the environment ID as a string when [creating a session](managed-agents/sessions.md).

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:sessions create --agent "$AGENT_ID" --environment-id "$ENVIRONMENT_ID"
```

##  Configuration options

###  Packages

The `packages` field pre-installs packages into the sandbox before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions. Unpinned packages install the latest version. If the environment uses `limited` [networking](#networking), also set `networking.allow_package_managers` to `true`; otherwise the request is rejected with a 400 error.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create < environment.yaml
```

environment.yaml



```shiki
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
```

Supported package managers:

| Field | Package manager | Example |
| --- | --- | --- |
| `apt` | System packages (apt-get) | `"graphviz"` |
| `cargo` | Rust (cargo) | `"hyperfine@1.18.0"` |
| `gem` | Ruby (gem) | `"rails:7.1.0"` |
| `go` | Go modules | `"golang.org/x/tools/cmd/goimports@latest"` |
| `npm` | Node.js (npm) | `"express@4.18.0"` |
| `pip` | Python (pip) | `"sqlalchemy==2.0.30"` |

###  Networking

The `networking` field controls the sandbox's outbound network access. It does not affect the `web_search` or `web_fetch` tools, which run on Anthropic's servers; to restrict the sites those tools can reach, set `allowed_domains` or `blocked_domains` on the tool's entry in the agent toolset. See [Restrict web search and web fetch domains](managed-agents/tools.md).

| Mode | Description |
| --- | --- |
| `unrestricted` | Full outbound network access, except for a general safety blocklist. This is the default. |
| `limited` | Restricts sandbox network access to the hosts in `allowed_hosts`. Set `allow_package_managers` and `allow_mcp_servers` to `true` to allow additional access. |

The following example creates an environment with `limited` networking:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:environments create < environment.yaml
```

environment.yaml



```shiki
name: api-access
config:
  type: cloud
  networking:
    type: limited
    allowed_hosts:
      - api.example.com
    allow_mcp_servers: true
    allow_package_managers: true
```

When using `limited` networking:

- `allowed_hosts` specifies domains the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`). Do not include a URL scheme, port, or path.
- `allow_mcp_servers` allows outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
- `allow_package_managers` allows outbound access to public package registries (such as PyPI and npm) beyond those listed in the `allowed_hosts` array. Defaults to `false`. Set it to `true` whenever the environment specifies `packages`; otherwise the request is rejected with a 400 error, even if the registry hosts are listed in `allowed_hosts`.

##  Environment lifecycle

- Environments persist until explicitly archived or deleted.
- Each session gets its own sandbox instance, even when multiple sessions reference the same environment. Sessions do not share filesystem state.
- Environments are not versioned. If you update an environment frequently, keep your own record of the changes so you can tell which configuration each session used.

##  Manage environments

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

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

Cloud sandboxes include common language runtimes, databases, and command-line tools out of the box. See [Cloud sandbox reference](managed-agents/cloud-sandboxes-reference.md) for the full list.

##  Next steps



[Cloud sandbox reference](managed-agents/cloud-sandboxes-reference.md)

Pre-installed packages, databases, and utilities available in cloud sandboxes.



[Start a session](managed-agents/sessions.md)

Create a session to run your agent and start running tasks.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
