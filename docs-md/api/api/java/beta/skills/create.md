# Create Skill

Copy page

Java

# Create Skill

[SkillCreateResponse](api/beta.md) beta().skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills

Create Skill

##### ParametersExpand Collapse

SkillCreateParams params

Optional<List<AnthropicBeta>> betas

Optional header to specify the beta version(s) you want to use.

MESSAGE\_BATCHES\_2024\_09\_24("message-batches-2024-09-24")

PROMPT\_CACHING\_2024\_07\_31("prompt-caching-2024-07-31")

COMPUTER\_USE\_2024\_10\_22("computer-use-2024-10-22")

COMPUTER\_USE\_2025\_01\_24("computer-use-2025-01-24")

PDFS\_2024\_09\_25("pdfs-2024-09-25")

TOKEN\_COUNTING\_2024\_11\_01("token-counting-2024-11-01")

TOKEN\_EFFICIENT\_TOOLS\_2025\_02\_19("token-efficient-tools-2025-02-19")

OUTPUT\_128K\_2025\_02\_19("output-128k-2025-02-19")

FILES\_API\_2025\_04\_14("files-api-2025-04-14")

MCP\_CLIENT\_2025\_04\_04("mcp-client-2025-04-04")

MCP\_CLIENT\_2025\_11\_20("mcp-client-2025-11-20")

DEV\_FULL\_THINKING\_2025\_05\_14("dev-full-thinking-2025-05-14")

INTERLEAVED\_THINKING\_2025\_05\_14("interleaved-thinking-2025-05-14")

CODE\_EXECUTION\_2025\_05\_22("code-execution-2025-05-22")

EXTENDED\_CACHE\_TTL\_2025\_04\_11("extended-cache-ttl-2025-04-11")

CONTEXT\_1M\_2025\_08\_07("context-1m-2025-08-07")

CONTEXT\_MANAGEMENT\_2025\_06\_27("context-management-2025-06-27")

MODEL\_CONTEXT\_WINDOW\_EXCEEDED\_2025\_08\_26("model-context-window-exceeded-2025-08-26")

SKILLS\_2025\_10\_02("skills-2025-10-02")

FAST\_MODE\_2026\_02\_01("fast-mode-2026-02-01")

Optional<String> displayTitle

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

Optional<List<String>> files

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

##### ReturnsExpand Collapse

class SkillCreateResponse:

String id

Unique identifier for the skill.

The format and length of IDs may change over time.

String createdAt

ISO 8601 timestamp of when the skill was created.

Optional<String> displayTitle

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

Optional<String> latestVersion

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

String source

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

String type

Object type.

For Skills, this is always `"skill"`.

String updatedAt

ISO 8601 timestamp of when the skill was last updated.

Create Skill

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillCreateParams;
import com.anthropic.models.beta.skills.SkillCreateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillCreateResponse skill = client.beta().skills().create();
    }
}
```

##### Returns Examples

---

*Copyright © Anthropic. All rights reserved.*
