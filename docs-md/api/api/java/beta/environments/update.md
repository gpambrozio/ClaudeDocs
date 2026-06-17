# Update Environment

Copy page



Java

# Update Environment

[BetaEnvironment](api/beta.md) beta().environments().update(EnvironmentUpdateParamsparams = EnvironmentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/environments/{environment\_id}

Update an existing environment's configuration.

##### ParametersExpand Collapse



EnvironmentUpdateParams params

Optional<String> environmentId



Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

USER\_PROFILES\_2026\_03\_24("user-profiles-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

MANAGED\_AGENTS\_2026\_04\_01("managed-agents-2026-04-01")

CACHE\_DIAGNOSIS\_2026\_04\_07("cache-diagnosis-2026-04-07")

THINKING\_TOKEN\_COUNT\_2026\_05\_13("thinking-token-count-2026-05-13")

SERVER\_SIDE\_FALLBACK\_2026\_06\_01("server-side-fallback-2026-06-01")

FALLBACK\_CREDIT\_2026\_06\_01("fallback-credit-2026-06-01")



Optional<Config> config

Updated environment configuration



class BetaCloudConfigParams:

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "cloud"constant"cloud"constant

Environment type



Optional<Networking> networking

Network configuration policy. Omit on update to preserve the existing value.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type



class BetaLimitedNetworkParams:

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

JsonValue; type "limited"constant"limited"constant

Network policy type

Optional<Boolean> allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<Boolean> allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Optional<List<String>> allowedHosts

Specifies domains the container can reach.



Optional<[BetaPackagesParams](api/beta.md)> packages

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

Optional<List<String>> apt

Ubuntu/Debian packages to install

Optional<List<String>> cargo

Rust packages to install

Optional<List<String>> gem

Ruby packages to install

Optional<List<String>> go

Go packages to install

Optional<List<String>> npm

Node.js packages to install

Optional<List<String>> pip

Python packages to install

Optional<Type> type

Package configuration type



class BetaSelfHostedConfigParams:

Request params for `self_hosted` environment configuration.

JsonValue; type "self\_hosted"constant"self\_hosted"constant

Environment type

Optional<String> description

Updated description of the environment

Optional<Metadata> metadata

User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

Optional<String> name

Updated name for the environment



Optional<Scope> scope

The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

ORGANIZATION("organization")

ACCOUNT("account")

##### ReturnsExpand Collapse



class BetaEnvironment:

Unified Environment resource for both cloud and self-hosted environments.

String id

Environment identifier (e.g., 'env\_...')

Optional<String> archivedAt

RFC 3339 timestamp when environment was archived, or null if not archived



Config config

Environment configuration (either Anthropic Cloud or self-hosted)

One of the following:



class BetaCloudConfig:

`cloud` environment configuration.



Networking networking

Network configuration policy.

One of the following:



class BetaUnrestrictedNetwork:

Unrestricted network access.

JsonValue; type "unrestricted"constant"unrestricted"constant

Network policy type



class BetaLimitedNetwork:

Limited network access.

boolean allowMcpServers

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

boolean allowPackageManagers

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

List<String> allowedHosts

Specifies domains the container can reach.

JsonValue; type "limited"constant"limited"constant

Network policy type



[BetaPackages](api/beta.md) packages

Package manager configuration.

List<String> apt

Ubuntu/Debian packages to install

List<String> cargo

Rust packages to install

List<String> gem

Ruby packages to install

List<String> go

Go packages to install

List<String> npm

Node.js packages to install

List<String> pip

Python packages to install

Optional<Type> type

Package configuration type

JsonValue; type "cloud"constant"cloud"constant

Environment type



class BetaSelfHostedConfig:

Configuration for self-hosted environments.

JsonValue; type "self\_hosted"constant"self\_hosted"constant

Environment type

String createdAt

RFC 3339 timestamp when environment was created

String description

User-provided description for the environment

Metadata metadata

User-provided metadata key-value pairs

String name

Human-readable name for the environment

JsonValue; type "environment"constant"environment"constant

The type of object (always 'environment')

String updatedAt

RFC 3339 timestamp when environment was last updated



Optional<Scope> scope

The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

One of the following:

ORGANIZATION("organization")

ACCOUNT("account")

Update Environment

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.BetaEnvironment;
import com.anthropic.models.beta.environments.EnvironmentUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaEnvironment betaEnvironment = client.beta().environments().update("env_011CZkZ9X2dpNyB7HsEFoRfW");
    }
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
