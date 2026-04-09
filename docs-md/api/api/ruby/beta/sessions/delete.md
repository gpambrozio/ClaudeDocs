# Delete Session

Copy page

Ruby

# Delete Session

beta.sessions.delete(session\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedSession](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}

Delete Session

##### ParametersExpand Collapse

session\_id: String

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

class BetaManagedAgentsDeletedSession { id, type }

Confirmation that a `session` has been permanently deleted.

id: String

type: :session\_deleted

Delete Session

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_session = anthropic.beta.sessions.delete("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_deleted_session)
```

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
