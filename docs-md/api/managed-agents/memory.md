# Using agent memory

Copy page

Each Managed Agents session starts with a fresh context by default. When a session ends, anything the agent learned is gone. Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDKs set the beta header automatically.

## Overview

A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When you attach a store to a session, it is mounted as a directory inside the session's container. The agent reads and writes it with the same file tools it uses for the rest of the filesystem, and a note describing each mount is automatically added to the system prompt so the agent knows where to look. The [agent toolset](managed-agents/tools.md) is required for these interactions; make sure to enable it during [agent creation](managed-agents/agent-setup.md).

Each **memory** in a store is addressed by a path and can be read and edited directly via the API or Console, allowing for tuning, importing, and exporting.

Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.

## Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
store = client.beta.memory_stores.create(
    name="User Preferences",
    description="Per-user preferences and project context.",
)
print(store.id)  # memstore_01Hx...
```

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.

### Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.memories.create(
    store.id,
    path="/formatting_standards.md",
    content="All reports use GAAP formatting. Dates are ISO-8601...",
)
```

Individual memories within the store are capped at 100KB (~25K tokens). Structure memory as many small focused files, not a few large ones.

## Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array when the session is created. Unlike file and repository resources, memory stores can only be attached at session creation time; adding or removing one from a running session is not supported.

Optionally include `instructions` to provide session-specific guidance for how the agent should use this store. It is shown to the agent alongside the store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write`, but `read_only` is also supported (shown explicitly in the example below).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "memory_store",
            "memory_store_id": store.id,
            "access": "read_write",
            "instructions": "User preferences and project context. Check before starting any task.",
        }
    ],
)
```

Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user-supplied prompts, fetched web content, or third-party tool output), a successful prompt injection could write malicious content into the store. Later sessions then read that content as trusted memory. Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material:** one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write store.
- **Mapping to your product's structure:** one store per end user, per team, or per project, while sharing a single agent configuration.
- **Different lifecycles:** a store that outlives any single session, or one you want to archive on its own schedule.

### How the agent accesses memory

Each attached store is mounted inside the session's container as a directory under `/mnt/memory/`, and the agent reads and writes it with the standard [agent toolset](managed-agents/tools.md). Writes are persisted back to the store and stay in sync across sessions that share it. A short description of each mount (path, access mode, store `description`, and any `instructions`) is automatically added to the system prompt.

`access` is enforced at the filesystem level: a `read_only` mount rejects writes, while writes to a `read_write` mount produce [memory versions](#audit-memory-changes) attributed to the session.

The agent's reads and writes appear in the [event stream](managed-agents/events-and-streaming.md) as ordinary `agent.tool_use` and `agent.tool_result` events for whichever tool touched the mount.

## View and edit memories

Memory stores can be managed directly via the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

### List memories

List the memories in a store, optionally filtered by `path_prefix` to browse a path like a directory:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
page = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix="/",
    order_by="path",
    depth=2,
)
for item in page.data:
    print(item.type, item.path)
```

See the [List memories reference](api/beta/memory_stores/memories/list.md) for full parameters and response schema.

### Read a memory

Fetching an individual memory returns the full content.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
retrieved = client.beta.memory_stores.memories.retrieve(
    mem.id,
    memory_store_id=store.id,
)
print(retrieved.content)
```

See the [Retrieve a memory reference](api/beta/memory_stores/memories/retrieve.md) for full parameters and response schema.

### Create a memory

`memories.create` creates a memory at a given `path`. Create does not overwrite; to change an existing memory, use [`memories.update`](#update-a-memory).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
mem = client.beta.memory_stores.memories.create(
    store.id,
    path="/preferences/formatting.md",
    content="Always use tabs, not spaces.",
)
```

See the [Create a memory reference](api/beta/memory_stores/memories/create.md) for full parameters and response schema.

### Update a memory

`memories.update()` modifies an existing memory by ID. You can change `content`, `path` (a rename), or both. The example renames a memory to an archive path:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.memories.update(
    mem.id,
    memory_store_id=store.id,
    path="/archive/2026_q1_formatting.md",
)
```

See the [Update a memory reference](api/beta/memory_stores/memories/update.md) for full parameters and response schema.

#### Safe content edits (optimistic concurrency)

To avoid clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored content hash still matches the one you read; on mismatch, re-read the memory and retry against the fresh state.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.memories.update(
    memory_id=mem.id,
    memory_store_id=store.id,
    content="CORRECTED: Always use 2-space indentation.",
    precondition={"type": "content_sha256", "content_sha256": mem.content_sha256},
)
```

### Delete a memory

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.memories.delete(
    mem.id,
    memory_store_id=store.id,
)
```

See the [Delete a memory reference](api/beta/memory_stores/memories/delete.md) for full parameters and response schema.

## Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Use the version endpoints to audit who changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

Versions belong to the store (not the individual memory) and survive even after the memory itself is deleted, so the audit trail stays complete. Versions are retained for 30 days; however, the recent versions are always kept regardless of age, so memories that change infrequently may retain history beyond 30 days. The live `memories.retrieve` call always returns the latest version; the version endpoints give you the retained history.

There is no dedicated restore endpoint; to roll back, retrieve the version you want and write its `content` back with `memories.update` (or `memories.create` if the parent memory has been deleted, since versions outlive their parent).

Past memory versions may be deleted after 30 days. If you'd like to preserve memory history for longer, export versions via the API.

### List versions

List version history for a store, newest first. The example filters to a single memory's history:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
versions = client.beta.memory_stores.memory_versions.list(
    store.id,
    memory_id=mem.id,
)
for v in versions:
    print(f"{v.id}: {v.operation}")

version_id = versions.data[1].id
```

See the [List memory versions reference](api/beta/memory_stores/memory_versions/list.md) for full parameters and response schema.

### Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
version = client.beta.memory_stores.memory_versions.retrieve(
    version_id,
    memory_store_id=store.id,
)
print(version.content)
```

See the [Retrieve a memory version reference](api/beta/memory_stores/memory_versions/retrieve.md) for full parameters and response schema.

### Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests.

A version that is the current head of a live memory cannot be redacted. Write a new version first (or delete the memory), then redact the old one.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.memory_versions.redact(
    version_id,
    memory_store_id=store.id,
)
```

See the [Redact a memory version reference](api/beta/memory_stores/memory_versions/redact.md) for full parameters and response schema.

## Manage memory stores

In addition to [`create`](api/beta/memory_stores/create.md), memory stores support [`retrieve`](api/beta/memory_stores/retrieve.md), [`update`](api/beta/memory_stores/update.md), [`list`](api/beta/memory_stores/list.md), [`archive`](api/beta/memory_stores/archive.md), and [`delete`](api/beta/memory_stores/delete.md).

### List stores

List stores in the workspace. Archived stores are excluded by default; pass `include_archived: true` to include them.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
for s in client.beta.memory_stores.list(include_archived=True):
    print(s.id, s.name, s.archived_at)
```

See the [List memory stores reference](api/beta/memory_stores/list.md) for full parameters and response schema.

### Archive a store

Archiving makes a store read-only and prevents it from being attached to new sessions. Archiving is one-way; there is no unarchive.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client.beta.memory_stores.archive(store.id)
```

See the [Archive a memory store reference](api/beta/memory_stores/archive.md) for full parameters and response schema.

To permanently remove a store along with all of its memories and versions, use [`memory_stores.delete`](api/beta/memory_stores/delete.md).

## Limits

Default capacity and rate limits apply to memory stores while this feature is in beta. [Contact support](https://support.claude.com) if you need higher limits.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
