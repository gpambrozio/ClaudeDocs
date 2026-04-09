# Delete Vault

Copy page

Python

# Delete Vault

beta.vaults.delete(strvault\_id, VaultDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedVault](api/beta.md)

DELETE/v1/vaults/{vault\_id}

Delete Vault

##### ParametersExpand Collapse

vault\_id: str

betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 18 more]

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

##### ReturnsExpand Collapse

class BetaManagedAgentsDeletedVault: …

Confirmation of a deleted vault.

id: str

Unique identifier of the deleted vault.

type: Literal["vault\_deleted"]

Delete Vault

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_deleted_vault = client.beta.vaults.delete(
    vault_id="vlt_011CZkZDLs7fYzm1hXNPeRjv",
)
print(beta_managed_agents_deleted_vault.id)
```

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
