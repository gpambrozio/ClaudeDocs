# Delete Credential

Copy page

Ruby

# Delete Credential

beta.vaults.credentials.delete(credential\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedCredential](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

Delete Credential

##### ParametersExpand Collapse

vault\_id: String

credential\_id: String

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

class BetaManagedAgentsDeletedCredential { id, type }

Confirmation of a deleted credential.

id: String

Unique identifier of the deleted credential.

type: :vault\_credential\_deleted

Delete Credential

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_credential = anthropic.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_deleted_credential)
```

Response 200

```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
