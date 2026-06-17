# Validate Credential

Copy page



Python

# Validate Credential

beta.vaults.credentials.mcp\_oauth\_validate(strcredential\_id, CredentialMCPOAuthValidateParams\*\*kwargs)  -> [BetaManagedAgentsCredentialValidation](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

vault\_id: str

credential\_id: str



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 25 more]

One of the following:

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

##### ReturnsExpand Collapse



class BetaManagedAgentsCredentialValidation: …

Result of live-probing a credential against its configured MCP server.

credential\_id: str

Unique identifier of the credential that was validated.

has\_refresh\_token: bool

Whether the credential has a refresh token configured.



mcp\_probe: Optional[BetaManagedAgentsMCPProbe]

The failing step of an MCP validation probe.



http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

method: str

The MCP method that failed (for example `initialize` or `tools/list`).



refresh: Optional[BetaManagedAgentsRefreshObject]

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.



status: Literal["succeeded", "failed", "connect\_error", "no\_refresh\_token"]

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



status: [BetaManagedAgentsCredentialValidationStatus](api/beta.md)

Overall verdict of a credential validation probe.

One of the following:

"valid"

"invalid"

"unknown"

type: Literal["vault\_credential\_validation"]

validated\_at: datetime

A timestamp in RFC 3339 format

vault\_id: str

Identifier of the vault containing the credential.

Validate Credential

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_credential_validation = client.beta.vaults.credentials.mcp_oauth_validate(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential_validation.credential_id)
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
