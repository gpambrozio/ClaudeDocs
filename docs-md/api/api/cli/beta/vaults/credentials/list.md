# List Credentials

Copy page

SDK language

CLI

# List Credentials

$ ant beta:vaults:credentials list

GET/v1/vaults/{vault\_id}/credentials

List Credentials

##### ParametersExpand Collapse

--vault-id: string

Path param: Path parameter vault\_id

--include-archived: optional boolean

Query param: Whether to include archived credentials in the results.

--limit: optional number

Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

--page: optional string

Query param: Opaque pagination token from a previous `list_credentials` response.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaManagedAgentsListCredentialsResponse: object { data, next\_page } 

Response containing a paginated list of credentials.



data: optional array of [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } 

List of credentials.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }  or [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta.md) { networking, secret\_name, type } 

Authentication details for a credential.



beta\_managed\_agents\_mcp\_oauth\_auth\_response: object { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type } 

Token endpoint uses POST body authentication with client credentials.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_static\_bearer\_auth\_response: object { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "static\_bearer"

"static\_bearer"



beta\_managed\_agents\_environment\_variable\_auth\_response: object { networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.



beta\_managed\_agents\_unrestricted\_credential\_networking\_response: object { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_response: object { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.



type: "limited"

"limited"

secret\_name: string

Name of the environment variable.



type: "environment\_variable"

"environment\_variable"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.



type: "vault\_credential"

"vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.

next\_page: optional string

Pagination token for the next page, or null if no more results.

List Credentials

CLI

```shiki
ant beta:vaults:credentials list \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
