# Delete Skill

Copy page

Ruby

# Delete Skill

beta.skills.delete(skill\_id, \*\*kwargs) -> [SkillDeleteResponse](api/beta.md) { id, type }

delete/v1/skills/{skill\_id}

Delete Skill

##### ParametersExpand Collapse

skill\_id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

anthropic\_beta: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 16 more

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

##### ReturnsExpand Collapse

class SkillDeleteResponse { id, type }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

type: String

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.delete("skill_id")

puts(skill)
```

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```