# Validate Credential

Copy page

C#

# Validate Credential

[BetaManagedAgentsCredentialValidation](api/beta.md) Beta.Vaults.Credentials.McpOAuthValidate(CredentialMcpOAuthValidateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

CredentialMcpOAuthValidateParams parameters

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

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

##### ReturnsExpand Collapse

class BetaManagedAgentsCredentialValidation:

Result of live-probing a credential against its configured MCP server.

required string CredentialID

Unique identifier of the credential that was validated.

required Boolean HasRefreshToken

Whether the credential has a refresh token configured.

required [BetaManagedAgentsMcpProbe](api/beta.md)? McpProbe

The failing step of an MCP validation probe.

required [BetaManagedAgentsRefreshHttpResponse](api/beta.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.

required string Method

The MCP method that failed (for example `initialize` or `tools/list`).

required [BetaManagedAgentsRefreshObject](api/beta.md)? Refresh

Outcome of a refresh-token exchange attempted during credential validation.

required [BetaManagedAgentsRefreshHttpResponse](api/beta.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.

required Status Status

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

"succeeded"Succeeded

"failed"Failed

"connect\_error"ConnectError

"no\_refresh\_token"NoRefreshToken

required [BetaManagedAgentsCredentialValidationStatus](api/beta.md) Status

Overall verdict of a credential validation probe.

Accepts one of the following:

"valid"Valid

"invalid"Invalid

"unknown"Unknown

required Type Type

required DateTimeOffset ValidatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault containing the credential.

Validate Credential

C#

```shiki
CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
```

Response 200

```shiki
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

##### Returns Examples

Response 200

```shiki
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

---

*Copyright © Anthropic. All rights reserved.*
