# Update Credential

Copy page

Go

# Update Credential

client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

Update Credential

##### ParametersExpand Collapse

credentialID string

params BetaVaultCredentialUpdateParams

VaultID param.Field[string]

Path param: Path parameter vault\_id

Auth param.Field[[BetaVaultCredentialUpdateParamsAuthUnion](api/beta/vaults/credentials/update.md)]optional

Body param: Updated authentication details for a credential.

type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

Type BetaManagedAgentsMCPOAuthUpdateParamsType

AccessToken stringoptional

Updated OAuth access token.

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp](api/beta.md)optional

Parameters for updating OAuth refresh token configuration.

RefreshToken stringoptional

Updated OAuth refresh token.

Scope stringoptional

Updated OAuth scope for the refresh request.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionRespoptional

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}

Updated HTTP Basic authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}

Updated POST body authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

Type BetaManagedAgentsStaticBearerUpdateParamsType

Token stringoptional

Updated static bearer token value.

DisplayName param.Field[string]optional

Body param: Updated human-readable name for the credential. 1-255 characters.

Metadata param.Field[map[string, string]]optional

Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

Betas param.Field[[]AnthropicBeta]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

type BetaManagedAgentsCredential struct{…}

A credential stored in a vault. Sensitive fields are never returned in responses.

ID string

Unique identifier for the credential.

ArchivedAt Time

A timestamp in RFC 3339 format

Auth BetaManagedAgentsCredentialAuthUnion

Authentication details for a credential.

Accepts one of the following:

type BetaManagedAgentsMCPOAuthAuthResponse struct{…}

OAuth credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsMCPOAuthAuthResponseType

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md)optional

OAuth refresh token configuration returned in credential responses.

ClientID string

OAuth client ID.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneResponseType

type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthBasicResponseType

type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}

Token endpoint uses POST body authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthPostResponseType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsStaticBearerAuthResponse struct{…}

Static bearer token credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsStaticBearerAuthResponseType

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

Arbitrary key-value metadata attached to the credential.

Type BetaManagedAgentsCredentialType

UpdatedAt Time

A timestamp in RFC 3339 format

VaultID string

Identifier of the vault this credential belongs to.

DisplayName stringoptional

Human-readable name for the credential.

Update Credential

Go

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
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Update(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialUpdateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
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
