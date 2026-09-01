# Tools

Copy page



Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a [session](managed-agents/sessions.md). You control which tools are available by specifying them in the agent configuration.

Claude Managed Agents also supports custom, user-defined tools. Your application executes these tools separately and returns the results to Claude, which uses them to continue the task. To give the agent tools from an MCP server, use the [MCP connector](managed-agents/mcp-connector.md) instead.

## Available tools

The agent toolset includes the following tools. All are enabled by default when you include the toolset in your agent configuration. Each entry in the `configs` array is identified by its `name`, using the values in the Name column, and accepts an optional `type` field with the same value. The `web_search` and `web_fetch` entries accept additional settings; see [Restrict web search and web fetch domains](#restrict-web-search-and-web-fetch-domains).

| Tool | Name | Description |
| --- | --- | --- |
| Bash | `bash` | Execute bash commands in a shell session |
| Read | `read` | Read a file from the sandbox filesystem |
| Write | `write` | Write a file to the sandbox filesystem |
| Edit | `edit` | Perform string replacement in a file |
| Glob | `glob` | Fast file pattern matching using glob patterns |
| Grep | `grep` | Text search using regex patterns |
| Web fetch | `web_fetch` | Fetch content from a URL |
| Web search | `web_search` | Search the web for information |

When a tool output exceeds 100,000 characters (about 25,000 tokens), it is automatically written to a file in the [sandbox](managed-agents/environments.md). The model receives a truncated preview with the file path and can read the full content from there.

## Configuring the toolset

Enable the full toolset with `agent_toolset_20260401` when creating an agent. Use the `configs` array to disable specific tools or override their settings. Each config entry can also set a `permission_policy` that controls whether the tool's calls are auto-approved or require confirmation. See [Permission policies](managed-agents/permission-policies.md) for the available policy types.

Config entries for `web_search` and `web_fetch` also accept domain filters and other web settings; see [Restrict web search and web fetch domains](#restrict-web-search-and-web-fetch-domains).

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-5
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_fetch
        enabled: false
YAML
```

### Disabling specific tools

To disable a tool, set `enabled: false` in its config entry in the toolset object of your agent's `tools` array:

```shiki
{
  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]
}
```



### Enabling only specific tools

The `default_config` object sets the baseline for every tool in the set, and per-tool `configs` entries override it. To start with everything off and enable only what you need, set `default_config.enabled` to `false`:

```shiki
{
  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]
}
```



### Restrict web search and web fetch domains

To control which sites the agent's web tools can reach, set `allowed_domains` (the tool can reach only these hosts) or `blocked_domains` (the tool can never reach these hosts) on the `web_search` and `web_fetch` entries of the toolset's `configs` array. Each tool carries its own list, so `web_search` and `web_fetch` can have different restrictions. A listed domain covers that host and all of its subdomains. At runtime, a `web_fetch` call for a URL that its lists do not permit returns an error result to the agent (`is_error: true` on the `agent.tool_result` event, with content that names the error code `url_not_allowed`), and `web_search` omits results that its lists do not permit.

The following toolset limits `web_search` to two sites and localizes its results, and blocks one host for `web_fetch` while capping how much fetched content enters the context:

```shiki
{
  "type": "agent_toolset_20260401",
  "configs": [
    {
      "type": "web_search",
      "name": "web_search",
      "allowed_domains": ["docs.example.com", "arxiv.org"],
      "user_location": {
        "type": "approximate",
        "country": "US",
        "timezone": "America/Los_Angeles"
      }
    },
    {
      "type": "web_fetch",
      "name": "web_fetch",
      "blocked_domains": ["ads.example.com"],
      "max_content_tokens": 50000
    }
  ]
}
```



The following request creates an agent with this toolset and prints the `configs` array from the response:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents create --transform tools.0.configs <<'YAML'
name: Research Agent
model: claude-opus-5
tools:
  - type: agent_toolset_20260401
    configs:
      - type: web_search
        name: web_search
        allowed_domains: [docs.example.com, arxiv.org]
        user_location:
          type: approximate
          country: US
          timezone: America/Los_Angeles
      - type: web_fetch
        name: web_fetch
        blocked_domains: [ads.example.com]
        max_content_tokens: 50000
YAML
```

In the Claude Console, set allowed or blocked domains from the `web_search` and `web_fetch` rows of the **Built-in tools** card on the agent form; set `max_content_tokens` and `user_location` in the **Raw** view of the agent's configuration.

In addition to `enabled` and `permission_policy`, the web tool entries accept the following settings:

| Setting | Applies to | Description |
| --- | --- | --- |
| `allowed_domains` | `web_search`, `web_fetch` | The only hosts the tool can reach. Cannot be combined with `blocked_domains` on the same entry. |
| `blocked_domains` | `web_search`, `web_fetch` | Hosts the tool cannot reach. |
| `max_content_tokens` | `web_fetch` | Caps the amount of fetched page content included in the context. Must be a positive integer. See [content limits](agents-and-tools/tool-use/web-fetch-tool.md). |
| `user_location` | `web_search` | Localizes search results. An object with the same fields as the Messages API [`user_location`](agents-and-tools/tool-use/web-search-tool.md) parameter. |

#### Domain list rules

- Set either `allowed_domains` or `blocked_domains` on an entry, not both. An entry that sets both is rejected.
- Each list holds 1 to 64 domains, each 1 to 255 characters. An empty list is rejected: to apply no restriction, omit the field or send `null`.
- Each domain is a registrable domain name, or a subdomain of one, written as a plain hostname: ASCII letters, digits, hyphens, underscores, and dots, with no scheme, port, credentials, wildcard, or whitespace, no label that begins or ends with a hyphen, and no path other than the optional `web_search` path suffix described later in this list. Use `example.com`, not `https://example.com`, `example.com:443`, or `*.example.com`. Hostnames are compared without regard to case, and a single trailing `/` is ignored.
- A listed domain matches that host and its subdomains: `example.com` covers `docs.example.com`, but `docs.example.com` does not cover `example.com` or `api.example.com`. A leading `www.` is a subdomain like any other, so `www.example.com` does not cover `example.com`; list the bare domain to cover both.
- IP addresses are not accepted in any form, whether IPv4, IPv6, bracketed, or numeric shorthand such as `127.1`. List the site's domain name instead.
- A bare top-level domain or registry suffix such as `com`, `co.uk`, or `gov.uk` is rejected, and so is a single-label name such as `intranet`. List a full domain such as `example.co.uk`.
- `localhost` and hosts ending in `.localhost`, `.local`, `.internal`, `.localdomain`, or `.invalid` are rejected.
- Use the `xn--` (Punycode) form for internationalized domain names; a domain that contains non-ASCII characters is rejected.
- A `web_fetch` domain cannot include a path: use `example.com`, not `example.com/*`. A `web_search` domain can carry a path suffix such as `example.com/blog`, in which the path cannot contain spaces, `?`, `#`, or any of the characters `$ , | ^ !`. Prefer plain hostnames for `web_search` too, because the search provider matches path suffixes as URL patterns rather than as strict host rules.
- Duplicate domains within a list are rejected. `www.example.com` and `example.com` count as different domains; see the earlier matching rule for what each covers.

#### When settings are validated

Format and limit violations are rejected with a 400 `invalid_request_error` when you [create an agent](managed-agents/agent-setup.md) or [update an agent](managed-agents/agent-setup.md), and when you create or update a session that supplies `tools`. For example, the message for an entry that sets both lists includes `Only one of allowed_domains or blocked_domains may be set.`, and the message for an empty list includes `allowed_domains: Empty list of domains is ambiguous. Provide at least one domain or null.` The message for a domain that breaks a format rule names its list and zero-based position, for example `allowed_domains.0: IP addresses are not supported; provide a plain hostname like "example.com"`.

The same requests also reject three settings that depend on the search and fetch providers: a domain in `allowed_domains` that Anthropic's crawler is not permitted to access, a `user_location.country` that the search provider does not support (the message ends in `user_location.country: not a country the search provider supports`), and a `user_location.timezone` that is not a valid IANA name. The session checks the configuration again when it first initializes the tool; if a setting that was accepted earlier is no longer valid at that point, the session emits a [`session.error`](managed-agents/events-and-streaming.md) event and returns to `idle` without retrying. Fix the setting by [updating the session's tools](managed-agents/session-operations.md), update the agent as well so that new sessions start with the corrected configuration, then send a new `user.message` to continue.

#### Multiagent sessions, outcomes, and mid-session updates

In a [multiagent session](managed-agents/multiagent-orchestration.md), every domain list that applies to a thread is enforced at the same time: an agent in the roster of the coordinator is bound by its own `allowed_domains` and `blocked_domains`, by those of any agent that called it, and by the coordinator's current lists.

- Allowlists combine to the domains that all of them cover, and blocklists add together, so a roster agent can narrow what a tool reaches but never widen it. For example, a roster agent that sets `blocked_domains` keeps the coordinator's `allowed_domains` and blocks those hosts within it, and a roster agent that sets its own `allowed_domains` can reach only the hosts that both its list and the coordinator's list cover.
- If the combined allowlists have no domain in common, the tool stays available to that agent but every call fails with a `url_not_allowed` error stating that no domain is permitted, and the tool description tells the model so. Keep each roster agent's allowlist inside the coordinator's to avoid this.
- `max_content_tokens` and `user_location` are not combined: a thread uses the value from its own tool configuration if set, otherwise from the agent that called it, otherwise from the coordinator's current configuration.
- A `{"type": "self"}` roster entry has no web settings of its own and follows the coordinator's current settings.
- The grader in [outcome-driven sessions](managed-agents/define-outcomes.md) runs without `web_search` and `web_fetch`, regardless of these settings.
- You can change the lists on an idle session by [updating its tools](managed-agents/session-operations.md). The new lists apply to the rest of the session; in a multiagent session, every thread applies them from its next turn, while a roster agent's own lists stay as its agent definition set them when the session was created.

#### Differences from the Messages API tools

These settings use the same `allowed_domains` and `blocked_domains` vocabulary as [domain filtering](agents-and-tools/tool-use/server-tools.md) on the Messages API server tools, with the following differences on Managed Agents:

- Each list is capped at 64 domains.
- Domains listed for `web_fetch` cannot include a path.
- Domains must be ASCII: use the `xn--` (Punycode) form for internationalized domain names. The Messages API accepts Unicode entries, though it recommends against them.
- `max_uses`, `citations`, and `cache_control` are not available on the toolset.

## Custom tools

In addition to built-in tools, you can define custom tools. Custom tools are analogous to [user-defined client tools](agents-and-tools/tool-use/how-tool-use-works.md) in the Messages API.

Each custom tool defines a contract: you specify what operations are available and what they return, and Claude determines when and how to call them. The model never executes anything on its own. It emits a structured request, your code runs the operation, and the result flows back into the conversation. See [Session event stream](managed-agents/events-and-streaming.md) for how to receive custom tool calls and return results during a session.

If your sessions run in a self-hosted sandbox, the environment worker can [serve custom tools from your sandbox](managed-agents/self-hosted-sandboxes.md), including tools that wrap an MCP server inside your network.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
ant beta:agents create < agent.yaml
```

agent.yaml



```shiki
name: Weather Agent
model: claude-opus-5
tools:
  - type: agent_toolset_20260401
  - type: custom
    name: get_weather
    description: Get current weather for a location
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: City name
      required:
        - location
```

Once you've defined custom tools on the agent, the agent invokes them during a session.

### Best practices for custom tool definitions

- **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain what the tool does and when to use it (and when not to). Explain what each parameter means and how it affects the tool's behavior. Call out any important caveats or limitations. The more context you can give Claude about your tools, the better it is at determining when and how to use them. Aim for three to four sentences for each tool description, more if the tool is complex.
- **Consolidate related operations into fewer tools.** Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
- **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the resource (for example, `db_query` or `storage_read`). This makes tool selection unambiguous as your library grows.
- **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (for example, slugs or UUIDs) rather than opaque internal references, and include only the fields Claude needs to determine its next step. Bloated responses waste context and make it harder for Claude to extract what matters.

## Next steps



[MCP connector](managed-agents/mcp-connector.md)

Connect MCP servers to your agents for access to external tools and data sources.



[Permission policies](managed-agents/permission-policies.md)

Control when agent and MCP tools execute.



[Session event stream](managed-agents/events-and-streaming.md)

Send events, stream responses, and interrupt or redirect your session mid-execution.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
