# Get Skill Version

Copy page



Ruby

# Get Skill Version

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta/skills/versions.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

Get Skill Version

##### ParametersExpand Collapse



skill\_id: String

Unique identifier for the skill.

The format and length of IDs may change over time.



version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 26 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

:"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class VersionRetrieveResponse { id, created\_at, description, 5 more } 



id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.



description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.



type: String

Object type.

For Skill Versions, this is always `"skill_version"`.



version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Get Skill Version

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.retrieve("version", skill_id: "skill_id")

puts(version)
```

Response 200



```shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

---

*Copyright © Anthropic. All rights reserved.*
