# Validate Credential

Copy page



TypeScript

# Validate Credential

client.beta.vaults.credentials.mcpOAuthValidate(stringcredentialID, CredentialMCPOAuthValidateParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

credentialID: string



params: CredentialMCPOAuthValidateParams { vault\_id, betas } 

vault\_id: string

Path param: Path parameter vault\_id



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 26 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



BetaManagedAgentsCredentialValidation { credential\_id, has\_refresh\_token, mcp\_probe, 5 more } 

Result of live-probing a credential against its configured MCP server.

credential\_id: string

Unique identifier of the credential that was validated.

has\_refresh\_token: boolean

Whether the credential has a refresh token configured.



mcp\_probe: [BetaManagedAgentsMCPProbe](api/beta/vaults/credentials.md) { http\_response, method }  | null

The failing step of an MCP validation probe.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md) { body, body\_truncated, content\_type, status\_code }  | null

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.

method: string

The MCP method that failed (for example `initialize` or `tools/list`).



refresh: [BetaManagedAgentsRefreshObject](api/beta/vaults/credentials.md) { http\_response, status }  | null

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md) { body, body\_truncated, content\_type, status\_code }  | null

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.



status: "succeeded" | "failed" | "connect\_error" | "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



status: [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md)

Overall verdict of a credential validation probe.

One of the following:

"valid"

"invalid"

"unknown"

type: "vault\_credential\_validation"

validated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault containing the credential.

Validate Credential

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsCredentialValidation = await client.beta.vaults.credentials.mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  { vault_id: 'vlt_011CZkZDLs7fYzm1hXNPeRjv' },
);

console.log(betaManagedAgentsCredentialValidation.credential_id);
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
