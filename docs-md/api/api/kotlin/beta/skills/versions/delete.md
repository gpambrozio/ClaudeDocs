# Delete Skill Version

Copy page

Kotlin

# Delete Skill Version

beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none()) : [VersionDeleteResponse](api/beta.md)

delete/v1/skills/{skill\_id}/versions/{version}

Delete Skill Version

##### ParametersExpand Collapse

params: VersionDeleteParams

skillId: String

Unique identifier for the skill.

The format and length of IDs may change over time.

version: Optional<String>

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

betas: Optional<List<AnthropicBeta>>

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

##### ReturnsExpand Collapse

class VersionDeleteResponse:

id: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

type: String

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

Delete Skill Version

Kotlin

```shiki
package com.anthropic.example

import com.anthropic.client.AnthropicClient
import com.anthropic.client.okhttp.AnthropicOkHttpClient
import com.anthropic.models.beta.skills.versions.VersionDeleteParams
import com.anthropic.models.beta.skills.versions.VersionDeleteResponse

fun main() {
    val client: AnthropicClient = AnthropicOkHttpClient.fromEnv()

    val params: VersionDeleteParams = VersionDeleteParams.builder()
        .skillId("skill_id")
        .version("version")
        .build()
    val version: VersionDeleteResponse = client.beta().skills().versions().delete(params)
}
```

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

---

*Copyright © Anthropic. All rights reserved.*
