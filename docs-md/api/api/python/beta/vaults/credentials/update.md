# Update Credential

Copy page

Python

# Update Credential

beta.vaults.credentials.update(strcredential\_id, CredentialUpdateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

Update Credential

##### ParametersExpand Collapse

vault\_id: str

credential\_id: str

auth: Optional[[Auth](api/beta/vaults/credentials/update.md)]

Updated authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMCPOAuthUpdateParams: …

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: Literal["mcp\_oauth"]

access\_token: Optional[str]

Updated OAuth access token.

expires\_at: Optional[datetime]

A timestamp in RFC 3339 format

refresh: Optional[BetaManagedAgentsMCPOAuthRefreshUpdateParams]

Parameters for updating OAuth refresh token configuration.

refresh\_token: Optional[str]

Updated OAuth refresh token.

scope: Optional[str]

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: Optional[TokenEndpointAuth]

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …

Updated HTTP Basic authentication parameters for the token endpoint.

type: Literal["client\_secret\_basic"]

client\_secret: Optional[str]

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …

Updated POST body authentication parameters for the token endpoint.

type: Literal["client\_secret\_post"]

client\_secret: Optional[str]

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerUpdateParams: …

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: Literal["static\_bearer"]

token: Optional[str]

Updated static bearer token value.

display\_name: Optional[str]

Updated human-readable name for the credential. 1-255 characters.

metadata: Optional[Dict[str, Optional[str]]]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 21 more]

Accepts one of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsCredential: …

A credential stored in a vault. Sensitive fields are never returned in responses.

id: str

Unique identifier for the credential.

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

auth: Auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMCPOAuthAuthResponse: …

OAuth credential details for an MCP server.

mcp\_server\_url: str

URL of the MCP server this credential authenticates against.

type: Literal["mcp\_oauth"]

expires\_at: Optional[datetime]

A timestamp in RFC 3339 format

refresh: Optional[BetaManagedAgentsMCPOAuthRefreshResponse]

OAuth refresh token configuration returned in credential responses.

client\_id: str

OAuth client ID.

token\_endpoint: str

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse: …

Token endpoint requires no client authentication.

type: Literal["none"]

class BetaManagedAgentsTokenEndpointAuthBasicResponse: …

Token endpoint uses HTTP Basic authentication with client credentials.

type: Literal["client\_secret\_basic"]

class BetaManagedAgentsTokenEndpointAuthPostResponse: …

Token endpoint uses POST body authentication with client credentials.

type: Literal["client\_secret\_post"]

resource: Optional[str]

OAuth resource indicator.

scope: Optional[str]

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse: …

Static bearer token credential details for an MCP server.

mcp\_server\_url: str

URL of the MCP server this credential authenticates against.

type: Literal["static\_bearer"]

created\_at: datetime

A timestamp in RFC 3339 format

metadata: Dict[str, str]

Arbitrary key-value metadata attached to the credential.

type: Literal["vault\_credential"]

updated\_at: datetime

A timestamp in RFC 3339 format

vault\_id: str

Identifier of the vault this credential belongs to.

display\_name: Optional[str]

Human-readable name for the credential.

Update Credential

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_credential = client.beta.vaults.credentials.update(
    credential_id="vcrd_011CZkZEMt8gZan2iYOQfSkw",
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_credential.id)
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
