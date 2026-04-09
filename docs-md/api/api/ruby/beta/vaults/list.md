# List Vaults

Copy page

Ruby

# List Vaults

beta.vaults.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

List Vaults

##### ParametersExpand Collapse

include\_archived: bool

Whether to include archived vaults in the results.

limit: Integer

Maximum number of vaults to return per page. Defaults to 20, maximum 100.

page: String

Opaque pagination token from a previous `list_vaults` response.

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

##### ReturnsExpand Collapse

class BetaManagedAgentsVault { id, archived\_at, created\_at, 4 more }

A vault that stores credentials for use by agents during sessions.

id: String

Unique identifier for the vault.

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

display\_name: String

Human-readable name for the vault.

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the vault.

type: :vault

updated\_at: Time

A timestamp in RFC 3339 format

List Vaults

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.list

puts(page)
```

Response 200

```shiki
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
