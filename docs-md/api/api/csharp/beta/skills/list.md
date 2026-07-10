# List Skills

Copy page



C#

# List Skills

[SkillListPageResponse](api/beta/skills.md) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

List Skills

##### ParametersExpand Collapse



SkillListParams parameters



Long limit

Query param: Number of results to return per page.

Maximum value is 100. Defaults to 20.



string? page

Query param: Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.



string? source

Query param: Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class SkillListPageResponse:



required IReadOnlyList<[SkillListResponse](api/beta/skills.md)> Data

List of skills.



required string ID

Unique identifier for the skill.

The format and length of IDs may change over time.

required string CreatedAt

ISO 8601 timestamp of when the skill was created.



required string? DisplayTitle

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



required string? LatestVersion

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



required string Source

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



required string Type

Object type.

For Skills, this is always `"skill"`.

required string UpdatedAt

ISO 8601 timestamp of when the skill was last updated.



required Boolean HasMore

Whether there are more results available.

If `true`, there are additional results that can be fetched using the `next_page` token.



required string? NextPage

Token for fetching the next page of results.

If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

List Skills

C#

```shiki
SkillListParams parameters = new();

var page = await client.Beta.Skills.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

Response 200



```shiki
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
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
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
