# Get Skill

Copy page



TypeScript

# Get Skill

client.beta.skills.retrieve(stringskillID, SkillRetrieveParams { betas } params?, RequestOptionsoptions?): [SkillRetrieveResponse](api/beta/skills.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

Get Skill

##### ParametersExpand Collapse



skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.



params: SkillRetrieveParams { betas } 



betas?: Array<[AnthropicBeta](api/beta.md)>

Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 26 more

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

SkillRetrieveResponse { id, created\_at, display\_title, 4 more } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.



display\_title: string | null

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



latest\_version: string | null

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.

Get Skill

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const skill = await client.beta.skills.retrieve('skill_id');

console.log(skill.id);
```

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
