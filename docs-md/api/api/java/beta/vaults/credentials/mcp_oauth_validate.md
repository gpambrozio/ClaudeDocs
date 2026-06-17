# Validate Credential

Copy page



Java

# Validate Credential

[BetaManagedAgentsCredentialValidation](api/beta.md) beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse



CredentialMcpOAuthValidateParams params

String vaultId

Optional<String> credentialId

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

##### ReturnsExpand Collapse



class BetaManagedAgentsCredentialValidation:

Result of live-probing a credential against its configured MCP server.

String credentialId

Unique identifier of the credential that was validated.

boolean hasRefreshToken

Whether the credential has a refresh token configured.



Optional<[BetaManagedAgentsMcpProbe](api/beta.md)> mcpProbe

The failing step of an MCP validation probe.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

String method

The MCP method that failed (for example `initialize` or `tools/list`).



Optional<[BetaManagedAgentsRefreshObject](api/beta.md)> refresh

Outcome of a refresh-token exchange attempted during credential validation.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.



Status status

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

SUCCEEDED("succeeded")

FAILED("failed")

CONNECT\_ERROR("connect\_error")

NO\_REFRESH\_TOKEN("no\_refresh\_token")



[BetaManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

One of the following:

VALID("valid")

INVALID("invalid")

UNKNOWN("unknown")

Type type

LocalDateTime validatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault containing the credential.

Validate Credential

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
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
