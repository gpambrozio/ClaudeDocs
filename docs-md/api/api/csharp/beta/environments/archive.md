# Archive Environment

Copy page



C#

# Archive Environment

[BetaEnvironment](api/beta/environments.md) Beta.Environments.Archive(EnvironmentArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/environments/{environment\_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

##### ParametersExpand Collapse



EnvironmentArchiveParams parameters

required string environmentID



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class BetaEnvironment:

Unified Environment resource for both cloud and self-hosted environments.

required string ID

Environment identifier (e.g., 'env\_...')

required string? ArchivedAt

RFC 3339 timestamp when environment was archived, or null if not archived



required Config Config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig:

`cloud` environment configuration.



required Networking Networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonElement Type "unrestricted"constant

Network policy type



class BetaLimitedNetwork:

Limited network access.

required Boolean AllowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

required Boolean AllowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

required IReadOnlyList<string> AllowedHosts

Specifies domains the container can reach.

JsonElement Type "limited"constant

Network policy type



required [BetaPackages](api/beta/environments.md) Packages

Package manager configuration.

required IReadOnlyList<string> Apt

Ubuntu/Debian packages to install

required IReadOnlyList<string> Cargo

Rust packages to install

required IReadOnlyList<string> Gem

Ruby packages to install

required IReadOnlyList<string> Go

Go packages to install

required IReadOnlyList<string> Npm

Node.js packages to install

required IReadOnlyList<string> Pip

Python packages to install

Type Type

Package configuration type

JsonElement Type "cloud"constant

Environment type



class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonElement Type "self\_hosted"constant

Environment type

required string CreatedAt

RFC 3339 timestamp when environment was created

required string Description

User-provided description for the environment

required IReadOnlyDictionary<string, string> Metadata

User-provided metadata key-value pairs

required string Name

Human-readable name for the environment

JsonElement Type "environment"constant

The type of object (always 'environment')

required string UpdatedAt

RFC 3339 timestamp when environment was last updated



Scope Scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

"organization"Organization

"account"Account

Archive Environment

C#

```shiki
EnvironmentArchiveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaEnvironment = await client.Beta.Environments.Archive(parameters);

Console.WriteLine(betaEnvironment);
```

Response 200



```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

---

*Copyright © Anthropic. All rights reserved.*
