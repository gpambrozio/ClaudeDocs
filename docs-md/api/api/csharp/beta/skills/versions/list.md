# List Skill Versions

Copy page



C#

# List Skill Versions

[VersionListPageResponse](api/beta.md) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### ParametersExpand Collapse



VersionListParams parameters



required string skillID

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.



Long? limit

Query param: Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

string? page

Query param: Optionally set to the `next_page` token from the previous response.

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

##### ReturnsExpand Collapse



class VersionListPageResponse:



required IReadOnlyList<[VersionListResponse](api/beta.md)> Data

List of skill versions.



required string ID

Unique identifier for the skill version.

The format and length of IDs may change over time.

required string CreatedAt

ISO 8601 timestamp of when the skill version was created.



required string Description

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



required string Directory

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



required string Name

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

required string SkillID

Identifier for the skill that this version belongs to.



required string Type

Object type.

For Skill Versions, this is always `"skill_version"`.



required string Version

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

required Boolean HasMore

Indicates if there are more results in the requested page direction.

required string? NextPage

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List Skill Versions

C#

```shiki
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
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
