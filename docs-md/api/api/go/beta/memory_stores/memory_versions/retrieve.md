# Retrieve a memory version

Copy page

Go

# Retrieve a memory version

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

Retrieve a memory version

##### ParametersExpand Collapse

memoryVersionID string

params BetaMemoryStoreMemoryVersionGetParams

MemoryStoreID param.Field[string]

Path param: Path parameter memory\_store\_id

View param.Field[[BetaManagedAgentsMemoryView](api/beta.md)]optional

Query param: Query parameter for view

Betas param.Field[[]AnthropicBeta]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

type BetaManagedAgentsMemoryVersion struct{…}

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

ID string

Unique identifier for this version (a `memver_...` value).

CreatedAt Time

A timestamp in RFC 3339 format

MemoryID string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

MemoryStoreID string

ID of the memory store this version belongs to (a `memstore_...` value).

Operation [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

Type BetaManagedAgentsMemoryVersionType

Content stringoptional

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

ContentSha256 stringoptional

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

ContentSizeBytes int64optional

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

CreatedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

Path stringoptional

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

RedactedAt Timeoptional

A timestamp in RFC 3339 format

RedactedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

Retrieve a memory version

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Get(
    context.TODO(),
    "memory_version_id",
    anthropic.BetaMemoryStoreMemoryVersionGetParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
```

Response 200

```shiki
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
```

##### Returns Examples

Response 200

```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
