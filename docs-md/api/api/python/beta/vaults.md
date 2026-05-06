# Vaults

Copy page

Python

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(VaultCreateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(VaultListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsVault](api/beta.md)]

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(strvault\_id, VaultRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(strvault\_id, VaultUpdateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(strvault\_id, VaultDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedVault](api/beta.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(strvault\_id, VaultArchiveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta.md)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault: …

Confirmation of a deleted vault.

id: str

Unique identifier of the deleted vault.

type: Literal["vault\_deleted"]

class BetaManagedAgentsVault: …

A vault that stores credentials for use by agents during sessions.

id: str

Unique identifier for the vault.

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

display\_name: str

Human-readable name for the vault.

metadata: Dict[str, str]

Arbitrary key-value metadata attached to the vault.

type: Literal["vault"]

updated\_at: datetime

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(strvault\_id, CredentialCreateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(strvault\_id, CredentialListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsCredential](api/beta.md)]

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(strcredential\_id, CredentialRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(strcredential\_id, CredentialUpdateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(strcredential\_id, CredentialDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedCredential](api/beta.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(strcredential\_id, CredentialArchiveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(strcredential\_id, CredentialMCPOAuthValidateParams\*\*kwargs)  -> [BetaManagedAgentsCredentialValidation](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse

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

class BetaManagedAgentsCredentialValidation: …

Result of live-probing a credential against its configured MCP server.

credential\_id: str

Unique identifier of the credential that was validated.

has\_refresh\_token: bool

Whether the credential has a refresh token configured.

mcp\_probe: Optional[BetaManagedAgentsMCPProbe]

The failing step of an MCP validation probe.

http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

method: str

The MCP method that failed (for example `initialize` or `tools/list`).

refresh: Optional[BetaManagedAgentsRefreshObject]

Outcome of a refresh-token exchange attempted during credential validation.

http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

status: Literal["succeeded", "failed", "connect\_error", "no\_refresh\_token"]

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"

status: [BetaManagedAgentsCredentialValidationStatus](api/beta.md)

Overall verdict of a credential validation probe.

Accepts one of the following:

"valid"

"invalid"

"unknown"

type: Literal["vault\_credential\_validation"]

validated\_at: datetime

A timestamp in RFC 3339 format

vault\_id: str

Identifier of the vault containing the credential.

Literal["valid", "invalid", "unknown"]

Overall verdict of a credential validation probe.

Accepts one of the following:

"valid"

"invalid"

"unknown"

class BetaManagedAgentsDeletedCredential: …

Confirmation of a deleted credential.

id: str

Unique identifier of the deleted credential.

type: Literal["vault\_credential\_deleted"]

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

class BetaManagedAgentsMCPOAuthCreateParams: …

Parameters for creating an MCP OAuth credential.

access\_token: str

OAuth access token.

mcp\_server\_url: str

URL of the MCP server this credential authenticates against.

type: Literal["mcp\_oauth"]

expires\_at: Optional[datetime]

A timestamp in RFC 3339 format

refresh: Optional[BetaManagedAgentsMCPOAuthRefreshParams]

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: str

OAuth client ID.

refresh\_token: str

OAuth refresh token.

token\_endpoint: str

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam: …

Token endpoint requires no client authentication.

type: Literal["none"]

class BetaManagedAgentsTokenEndpointAuthBasicParam: …

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_basic"]

class BetaManagedAgentsTokenEndpointAuthPostParam: …

Token endpoint uses POST body authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_post"]

resource: Optional[str]

OAuth resource indicator.

scope: Optional[str]

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshParams: …

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: str

OAuth client ID.

refresh\_token: str

OAuth refresh token.

token\_endpoint: str

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam: …

Token endpoint requires no client authentication.

type: Literal["none"]

class BetaManagedAgentsTokenEndpointAuthBasicParam: …

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_basic"]

class BetaManagedAgentsTokenEndpointAuthPostParam: …

Token endpoint uses POST body authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_post"]

resource: Optional[str]

OAuth resource indicator.

scope: Optional[str]

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshResponse: …

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

class BetaManagedAgentsMCPOAuthRefreshUpdateParams: …

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

class BetaManagedAgentsMCPProbe: …

The failing step of an MCP validation probe.

http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

method: str

The MCP method that failed (for example `initialize` or `tools/list`).

class BetaManagedAgentsRefreshHTTPResponse: …

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

class BetaManagedAgentsRefreshObject: …

Outcome of a refresh-token exchange attempted during credential validation.

http\_response: Optional[BetaManagedAgentsRefreshHTTPResponse]

An HTTP response captured during a credential validation probe.

body: str

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: str

Value of the `Content-Type` response header.

status\_code: int

HTTP status code.

status: Literal["succeeded", "failed", "connect\_error", "no\_refresh\_token"]

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"

class BetaManagedAgentsStaticBearerAuthResponse: …

Static bearer token credential details for an MCP server.

mcp\_server\_url: str

URL of the MCP server this credential authenticates against.

type: Literal["static\_bearer"]

class BetaManagedAgentsStaticBearerCreateParams: …

Parameters for creating a static bearer token credential.

token: str

Static bearer token value.

mcp\_server\_url: str

URL of the MCP server this credential authenticates against.

type: Literal["static\_bearer"]

class BetaManagedAgentsStaticBearerUpdateParams: …

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: Literal["static\_bearer"]

token: Optional[str]

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam: …

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_basic"]

class BetaManagedAgentsTokenEndpointAuthBasicResponse: …

Token endpoint uses HTTP Basic authentication with client credentials.

type: Literal["client\_secret\_basic"]

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam: …

Updated HTTP Basic authentication parameters for the token endpoint.

type: Literal["client\_secret\_basic"]

client\_secret: Optional[str]

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam: …

Token endpoint requires no client authentication.

type: Literal["none"]

class BetaManagedAgentsTokenEndpointAuthNoneResponse: …

Token endpoint requires no client authentication.

type: Literal["none"]

class BetaManagedAgentsTokenEndpointAuthPostParam: …

Token endpoint uses POST body authentication with client credentials.

client\_secret: str

OAuth client secret.

type: Literal["client\_secret\_post"]

class BetaManagedAgentsTokenEndpointAuthPostResponse: …

Token endpoint uses POST body authentication with client credentials.

type: Literal["client\_secret\_post"]

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam: …

Updated POST body authentication parameters for the token endpoint.

type: Literal["client\_secret\_post"]

client\_secret: Optional[str]

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
