# List Skill Versions

Copy page



Python

# List Skill Versions

beta.skills.versions.list(strskill\_id, VersionListParams\*\*kwargs)  -> SyncPageCursor[[VersionListResponse](api/beta/skills/versions.md)]

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### ParametersExpand Collapse



skill\_id: str

Unique identifier for the skill.

The format and length of IDs may change over time.



limit: Optional[int]

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

page: Optional[str]

Optionally set to the `next_page` token from the previous response.



betas: Optional[List[[AnthropicBetaParam](api/beta.md)]]

Optional header to specify the beta version(s) you want to use.

One of the following:

str



Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 26 more]

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"

##### ReturnsExpand Collapse



class VersionListResponse: …



id: str

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: str

ISO 8601 timestamp of when the skill version was created.



description: str

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: str

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: str

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: str

Identifier for the skill that this version belongs to.



type: str

Object type.

For Skill Versions, this is always `"skill_version"`.



version: str

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

List Skill Versions

Python

```shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.skills.versions.list(
    skill_id="skill_id",
)
page = page.data[0]
print(page.id)
```

Response 200



```shiki
{
  "data": [
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
  ],
  "has_more": true,
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
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
