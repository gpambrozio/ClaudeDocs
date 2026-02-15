# Create Skill Version

Copy page

C#

# Create Skill Version

[VersionCreateResponse](api/beta.md) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill\_id}/versions

Create Skill Version

##### ParametersExpand Collapse

VersionCreateParams parameters

required string skillID

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.

IReadOnlyList<string>? files

Body param: Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

##### ReturnsExpand Collapse

class VersionCreateResponse:

required string ID

Unique identifier for the skill version.

The format and length of IDs may change over time.

required string CreatedAt

ISO 8601 timestamp of when the skill version was created.

required string Description

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

required string Directory

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

required string Name

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

required string SkillID

Identifier for the skill that this version belongs to.

required string Type

Object type.

For Skill Versions, this is always `"skill_version"`.

required string Version

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

Create Skill Version

C#

```shiki
VersionCreateParams parameters = new() { SkillID = "skill_id" };

var version = await client.Beta.Skills.Versions.Create(parameters);

Console.WriteLine(version);
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
