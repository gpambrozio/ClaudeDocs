# Validate Credential

Copy page

CLI

# Validate Credential

$ ant beta:vaults:credentials mcp-oauth-validate

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

Validate Credential

##### ParametersExpand Collapse

--vault-id: string

Path param: Path parameter vault\_id

--credential-id: string

Path param: Path parameter credential\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_credential\_validation: object { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

Result of live-probing a credential against its configured MCP server.

credential\_id: string

Unique identifier of the credential that was validated.

has\_refresh\_token: boolean

Whether the credential has a refresh token configured.

mcp\_probe: object { http\_response, method }

The failing step of an MCP validation probe.

http\_response: object { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.

method: string

The MCP method that failed (for example `initialize` or `tools/list`).

refresh: object { http\_response, status }

Outcome of a refresh-token exchange attempted during credential validation.

http\_response: object { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.

status: "succeeded" or "failed" or "connect\_error" or "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"

status: "valid" or "invalid" or "unknown"

Overall verdict of a credential validation probe.

"valid"

"invalid"

"unknown"

type: "vault\_credential\_validation"

"vault\_credential\_validation"

validated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault containing the credential.

Validate Credential

CLI

```shiki
ant beta:vaults:credentials mcp-oauth-validate \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
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
