# Create Credential

Copy page



Java

# Create Credential

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials

Create Credential

##### ParametersExpand Collapse



CredentialCreateParams params

Optional<String> vaultId

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

Auth auth

Authentication details for creating a credential.



class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

String accessToken

OAuth access token.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)> refresh

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

String token

Static bearer token value.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type



class BetaManagedAgentsEnvironmentVariableCreateParams:

Parameters for creating an environment variable credential.



[BetaManagedAgentsCredentialNetworkingParams](api/beta.md) networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type

String secretName

Name of the environment variable. Immutable after create.

String secretValue

Secret value. Write-only; never returned in responses.

Type type

Optional<String> displayName

Human-readable name for the credential. Up to 255 characters.

Optional<Metadata> metadata

Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

##### ReturnsExpand Collapse



class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

String id

Unique identifier for the credential.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format



Auth auth

Authentication details for a credential.

One of the following:



class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type



class BetaManagedAgentsEnvironmentVariableAuthResponse:

Environment variable credential details. The secret value is never returned.



Networking networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type

String secretName

Name of the environment variable.

Type type

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata attached to the credential.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault this credential belongs to.

Optional<String> displayName

Human-readable name for the credential.

Create Credential

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsStaticBearerCreateParams;
import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
                .token("bearer_exampletoken")
                .mcpServerUrl("https://example-server.modelcontextprotocol.io/sse")
                .type(BetaManagedAgentsStaticBearerCreateParams.Type.STATIC_BEARER)
                .build())
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().create(params);
    }
}
```

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

---

*Copyright © Anthropic. All rights reserved.*
