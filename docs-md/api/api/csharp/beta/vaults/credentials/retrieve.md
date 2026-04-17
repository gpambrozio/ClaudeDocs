# Get Credential

Copy page

C#

# Get Credential

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

Get Credential

##### ParametersExpand Collapse

CredentialRetrieveParams parameters

required string vaultID

Path param: Path parameter vault\_id

required string credentialID

Path param: Path parameter credential\_id

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

##### ReturnsExpand Collapse

class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

required string ID

Unique identifier for the credential.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required Auth Auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the credential.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault this credential belongs to.

string? DisplayName

Human-readable name for the credential.

Get Credential

C#

```shiki
CredentialRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

Response 200

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
