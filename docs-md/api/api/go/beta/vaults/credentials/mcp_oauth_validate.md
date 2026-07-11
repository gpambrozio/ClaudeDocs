# Validate Credential

Copy page



Go

# Validate Credential

client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (\*[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

credentialID string



params BetaVaultCredentialMCPOAuthValidateParams

VaultID param.Field[string]

Path param: Path parameter vault\_id

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

type BetaManagedAgentsCredentialValidation struct{…}

Result of live-probing a credential against its configured MCP server.

CredentialID string

Unique identifier of the credential that was validated.

HasRefreshToken bool

Whether the credential has a refresh token configured.



MCPProbe [BetaManagedAgentsMCPProbe](api/beta/vaults/credentials.md)

The failing step of an MCP validation probe.



HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

Method string

The MCP method that failed (for example `initialize` or `tools/list`).



Refresh [BetaManagedAgentsRefreshObject](api/beta/vaults/credentials.md)

Outcome of a refresh-token exchange attempted during credential validation.



HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.



Status BetaManagedAgentsRefreshObjectStatus

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"

const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"

const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect\_error"

const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no\_refresh\_token"



Status [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md)

Overall verdict of a credential validation probe.

One of the following:

const BetaManagedAgentsCredentialValidationStatusValid [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md) = "valid"

const BetaManagedAgentsCredentialValidationStatusInvalid [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md) = "invalid"

const BetaManagedAgentsCredentialValidationStatusUnknown [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md) = "unknown"

Type BetaManagedAgentsCredentialValidationType

ValidatedAt Time

A timestamp in RFC 3339 format

VaultID string

Identifier of the vault containing the credential.

Validate Credential

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
  betaManagedAgentsCredentialValidation, err := client.Beta.Vaults.Credentials.MCPOAuthValidate(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialMCPOAuthValidateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredentialValidation.CredentialID)
}
```

Response 200



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



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
