# List Skills

Copy page

Ruby

# List Skills

beta.skills.list(\*\*kwargs) -> PageCursor<[SkillListResponse](api/beta.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

List Skills

##### ParametersExpand Collapse

limit: Integer

Number of results to return per page.

Maximum value is 100. Defaults to 20.

page: String

Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.

source: String

Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

anthropic\_beta: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 17 more

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

##### ReturnsExpand Collapse

class SkillListResponse { id, created\_at, display\_title, 4 more }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill was created.

display\_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: String

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: String

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: String

Object type.

For Skills, this is always `"skill"`.

updated\_at: String

ISO 8601 timestamp of when the skill was last updated.

List Skills

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.list

puts(page)
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
