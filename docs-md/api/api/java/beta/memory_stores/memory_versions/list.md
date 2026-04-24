# ListMemoryVersions

Copy page

Java

# ListMemoryVersions

MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

ListMemoryVersions

##### ParametersExpand Collapse

MemoryVersionListParams params

Optional<String> memoryStoreId

Optional<String> apiKeyId

Query parameter for api\_key\_id

Optional<LocalDateTime> createdAtGte

Return versions created at or after this time (inclusive).

Optional<LocalDateTime> createdAtLte

Return versions created at or before this time (inclusive).

Optional<Long> limit

Query parameter for limit

Optional<String> memoryId

Query parameter for memory\_id

Optional<[BetaManagedAgentsMemoryVersionOperation](api/beta.md)> operation

Query parameter for operation

Optional<String> page

Query parameter for page

Optional<String> sessionId

Query parameter for session\_id

Optional<[BetaManagedAgentsMemoryView](api/beta.md)> view

Query parameter for view

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

OUTPUT\_300K\_2026\_03\_24("output-300k-2026-03-24")

ADVISOR\_TOOL\_2026\_03\_01("advisor-tool-2026-03-01")

##### ReturnsExpand Collapse

class BetaManagedAgentsMemoryVersion:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryId

String memoryStoreId

[BetaManagedAgentsMemoryVersionOperation](api/beta.md) operation

MemoryVersionOperation enum

Accepts one of the following:

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

Type type

Optional<String> content

Optional<String> contentSha256

Optional<Long> contentSizeBytes

Optional<[BetaManagedAgentsActor](api/beta.md)> createdBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

Optional<String> path

Optional<LocalDateTime> redactedAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsActor](api/beta.md)> redactedBy

Accepts one of the following:

class BetaManagedAgentsSessionActor:

String sessionId

Type type

class BetaManagedAgentsApiActor:

String apiKeyId

Type type

class BetaManagedAgentsUserActor:

Type type

String userId

ListMemoryVersions

Java

```shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListPage;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionListPage page = client.beta().memoryStores().memoryVersions().list("memory_store_id");
    }
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
