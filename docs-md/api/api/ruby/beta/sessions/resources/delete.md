# Delete Session Resource

Copy page

Ruby

# Delete Session Resource

beta.sessions.resources.delete(resource\_id, \*\*kwargs) -> [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

Delete Session Resource

##### ParametersExpand Collapse

session\_id: String

resource\_id: String

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 20 more

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

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: String

type: :session\_resource\_deleted

Delete Session Resource

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_delete_session_resource = anthropic.beta.sessions.resources.delete(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_delete_session_resource)
```

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
