# Create Environment

Copy page



Go

# Create Environment

client.Beta.Environments.New(ctx, params) (\*[BetaEnvironment](api/beta/environments.md), error)

POST/v1/environments

Create a new environment with the specified configuration.

##### ParametersExpand Collapse



params BetaEnvironmentNewParams

Name param.Field[string]

Body param: Human-readable name for the environment



Config param.Field[[BetaEnvironmentNewParamsConfigUnion](api/beta/environments/create.md)]Optional

Body param: Environment configuration



type BetaCloudConfigParamsResp struct{…}

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Cloud

Environment type



Networking BetaCloudConfigParamsNetworkingUnionRespOptional

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type



type BetaLimitedNetworkParamsResp struct{…}

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

Type Limited

Network policy type

AllowMCPServers boolOptional

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowPackageManagers boolOptional

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

AllowedHosts []stringOptional

Specifies domains the container can reach.



Packages [BetaPackagesParamsResp](api/beta/environments.md)Optional

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Apt []stringOptional

Ubuntu/Debian packages to install

Cargo []stringOptional

Rust packages to install

Gem []stringOptional

Ruby packages to install

Go []stringOptional

Go packages to install

Npm []stringOptional

Node.js packages to install

Pip []stringOptional

Python packages to install

Type BetaPackagesParamsTypeOptional

Package configuration type



type BetaSelfHostedConfigParamsResp struct{…}

Request params for `self_hosted` environment configuration.

Type SelfHosted

Environment type

Description param.Field[string]Optional

Body param: Optional description of the environment

Metadata param.Field[map[string, string]]Optional

Body param: User-provided metadata key-value pairs



Scope param.Field[[BetaEnvironmentNewParamsScope](api/beta/environments/create.md)]Optional

Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

const BetaEnvironmentNewParamsScopeOrganization [BetaEnvironmentNewParamsScope](api/beta/environments/create.md) = "organization"

const BetaEnvironmentNewParamsScopeAccount [BetaEnvironmentNewParamsScope](api/beta/environments/create.md) = "account"



Betas param.Field[[]AnthropicBeta]Optional

Header param: Optional header to specify the beta version(s) you want to use.

string



type AnthropicBeta string

One of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaManagedAgents2026\_04\_01 AnthropicBeta = "managed-agents-2026-04-01"

const AnthropicBetaCacheDiagnosis2026\_04\_07 AnthropicBeta = "cache-diagnosis-2026-04-07"

const AnthropicBetaThinkingTokenCount2026\_05\_13 AnthropicBeta = "thinking-token-count-2026-05-13"

const AnthropicBetaServerSideFallback2026\_06\_01 AnthropicBeta = "server-side-fallback-2026-06-01"

const AnthropicBetaFallbackCredit2026\_06\_01 AnthropicBeta = "fallback-credit-2026-06-01"

const AnthropicBetaAgentMemory2026\_07\_22 AnthropicBeta = "agent-memory-2026-07-22"

##### ReturnsExpand Collapse



type BetaEnvironment struct{…}

Unified Environment resource for both cloud and self-hosted environments.

ID string

Environment identifier (e.g., 'env\_...')

ArchivedAt string

RFC 3339 timestamp when environment was archived, or null if not archived



Config BetaEnvironmentConfigUnion

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



type BetaCloudConfig struct{…}

`cloud` environment configuration.



Networking BetaCloudConfigNetworkingUnion

Network configuration policy.

One of the following:



type BetaUnrestrictedNetwork struct{…}

Unrestricted network access.

Type Unrestricted

Network policy type



type BetaLimitedNetwork struct{…}

Limited network access.

AllowMCPServers bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

AllowPackageManagers bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

AllowedHosts []string

Specifies domains the container can reach.

Type Limited

Network policy type



Packages [BetaPackages](api/beta/environments.md)

Package manager configuration.

Apt []string

Ubuntu/Debian packages to install

Cargo []string

Rust packages to install

Gem []string

Ruby packages to install

Go []string

Go packages to install

Npm []string

Node.js packages to install

Pip []string

Python packages to install

Type BetaPackagesTypeOptional

Package configuration type

Type Cloud

Environment type



type BetaSelfHostedConfig struct{…}

Configuration for self-hosted environments.

Type SelfHosted

Environment type

CreatedAt string

RFC 3339 timestamp when environment was created

Description string

User-provided description for the environment

Metadata map[string, string]

User-provided metadata key-value pairs

Name string

Human-readable name for the environment

Type Environment

The type of object (always 'environment')

UpdatedAt string

RFC 3339 timestamp when environment was last updated



Scope BetaEnvironmentScopeOptional

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"

const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"

Create Environment

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaEnvironment, err := client.Beta.Environments.New(context.TODO(), anthropic.BetaEnvironmentNewParams{
    Name: "python-data-analysis",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaEnvironment.ID)
}
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
