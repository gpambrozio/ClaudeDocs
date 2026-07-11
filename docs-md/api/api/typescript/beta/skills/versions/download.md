# Download Skill Version Content

Copy page



TypeScript

# Download Skill Version Content

client.beta.skills.versions.download(stringversion, VersionDownloadParams { skill\_id, betas } params, RequestOptionsoptions?): Response

GET/v1/skills/{skill\_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### ParametersExpand Collapse



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").



params: VersionDownloadParams { skill\_id, betas } 



skill\_id: string

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

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

unnamed\_schema\_3 = Response

Download Skill Version Content

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.skills.versions.download('version', { skill_id: 'skill_id' });

console.log(response);

const content = await response.blob();
console.log(content);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
