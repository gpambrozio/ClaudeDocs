# Create Skill Version

Copy page



cURL

# Create Skill Version

POST/v1/skills/{skill\_id}/versions

Create Skill Version

##### Path ParametersExpand Collapse



skill\_id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 26 more

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

##### Body ParametersForm DataExpand Collapse



files: array of string

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

##### ReturnsExpand Collapse



id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.



type: string

Object type.

For Skill Versions, this is always `"skill_version"`.



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Create Skill Version

cURL

```shiki
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: skills-2025-10-02' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
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
