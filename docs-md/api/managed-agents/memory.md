# Using agent memory

Copy page

Agent Memory is a Research Preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.

Managed Agents API sessions are ephemeral by default. When a session ends, anything the agent learned is gone. Memory stores let the agent carry learnings across sessions: user preferences, project conventions, prior mistakes, and domain context.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. An additional beta header is needed for research preview features. The SDK sets these beta headers automatically.

## Overview

A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When one or more memory stores are attached to a session, the agent automatically checks the stores before starting a task and writes durable learnings when done - no additional prompting or configuration is needed on your side.

Each **memory** in a store can be accessed and edited directly via the API or Console, allowing for tuning, importing, and exporting memories.

Every change to a memory creates an immutable **memory version** to support auditing and rolling back memory changes.

## Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
store=$(curl -fsS https://api.anthropic.com/v1/memory_stores \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<EOF
{
  "name": "User Preferences",
  "description": "Per-user preferences and project context."
}
EOF
)
store_id=$(jq -r '.id' <<< "$store")
echo "$store_id"  # memstore_01Hx...
```

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.

### Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- > /dev/null <<EOF
{
  "path": "/formatting_standards.md",
  "content": "All reports use GAAP formatting. Dates are ISO-8601..."
}
EOF
```

Individual memories within the store are capped at 100KB (~25K tokens). Structure memory as many small focused files, not a few large ones.

## Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array.

Optionally include a `prompt` if you want to provide session-specific instructions to Claude for how to use this memory store. It is provided to Claude in addition to the memory store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write`, but `read_only` is also supported (shown explicitly in the example below).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
session=$(curl -fsS https://api.anthropic.com/v1/sessions \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<EOF
{
  "agent": "$agent_id",
  "environment_id": "$environment_id",
  "resources": [
    {
      "type": "memory_store",
      "memory_store_id": "$store_id",
      "access": "read_write",
      "prompt": "User preferences and project context. Check before starting any task."
    }
  ]
}
EOF
)
```

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material** - one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write learnings.
- **Mapping to your product's structure** - one store per end-user, per-team, or per-project, while sharing a single agent configuration.
- **Different lifecycles** - a store that outlives any single session, or one you want to archive on its own schedule.

### Memory tools

When memory stores are attached to a session, the agent automatically gains access to memory tools. The agent's interactions with memory stores are registered as `agent.tool_use` events in the [event stream](managed-agents/events-and-streaming.md).

| Tool | Description |
| --- | --- |
| `memory_list` | List memories in a store, optionally filtered by path prefix. |
| `memory_search` | Full-text search across memory contents. |
| `memory_read` | Read a memory's contents. |
| `memory_write` | Create or overwrite a memory at a path. |
| `memory_edit` | Modify an existing memory. |
| `memory_delete` | Remove a memory. |

## View and edit memories

Memory stores can be managed directly via the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

### List memories

List does not return memory content, just object metadata. Use `path_prefix` for directory-scoped lists (include a trailing slash: `/notes/` matches `/notes/a.md` but not `/notes_backup/old.md`).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
page=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories?path_prefix=/" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")
jq -r '.data[] | "\(.path)  (\(.size_bytes) bytes, sha=\(.content_sha256[0:8]))"' <<< "$page"
```

### Read a memory

Fetching an individual memory returns the full content.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
mem=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$memory_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01")
jq -r '.content' <<< "$mem"
```

### Create a memory

Use `memories.write` to upsert a memory **by path**. If nothing exists at the path, it is created; if a memory already exists there, its content is replaced. To mutate an existing memory **by `mem_...` ID** (for example, to rename its path or safely apply a content edit), use `memories.update` instead (see [Update a memory](#update-a-memory) below).

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
mem=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- <<EOF
{
  "path": "/preferences/formatting.md",
  "content": "Always use tabs, not spaces."
}
EOF
)
```

#### Safe writes (optimistic concurrency)

Pass `precondition={"type": "not_exists"}` to `memories.write` to make it a create-only guard. If a memory already exists at the path, the write returns `409 memory_precondition_failed` instead of replacing it. Use this when seeding a store and you want to avoid clobbering existing content.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- > /dev/null <<EOF
{
  "path": "/preferences/formatting.md",
  "content": "Always use 2-space indentation.",
  "precondition": {"type": "not_exists"}
}
EOF
```

To safely edit an existing memory (read, modify, write back without clobbering a concurrent change), use `memories.update` with a `content_sha256` precondition instead. See [Update a memory](#update-a-memory) below.

### Update a memory

`memories.update()` modifies an existing memory by its `mem_...` ID. You can change `content`, `path` (a rename), or both in one call.

Renaming onto an occupied path returns `409 conflict`. The caller must delete or rename the blocker first, or pass `precondition={"type": "not_exists"}` to make the rename a no-op if anything already exists at the target.

The example below renames a memory to an archive path:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS -X PATCH "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{"path": "/archive/2026_q1_formatting.md"}' > /dev/null
```

#### Safe content edits (optimistic concurrency)

To edit a memory's content without clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored hash still matches the one you read; on mismatch it returns `409 memory_precondition_failed`, at which point you re-read the memory and retry against the fresh state.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS -X PATCH "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  --data @- > /dev/null <<EOF
{
  "content": "CORRECTED: Always use 2-space indentation.",
  "precondition": {"type": "content_sha256", "content_sha256": "$mem_sha"}
}
EOF
```

### Delete a memory

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS -X DELETE "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" > /dev/null
```

Optionally pass `expected_content_sha256` for a conditional delete.

## Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Versions accumulate for the lifetime of the parent memory and form the audit and rollback surface underneath it. The live `memories.retrieve` call always returns the current head; the version endpoints give you the full history.

A new version is written on every mutation:

- The first `memories.write` to a path creates a version with `operation: "created"`.
- `memories.update` that changes `content`, `path`, or both creates a version with `operation: "modified"`.
- `memories.delete` creates a version with `operation: "deleted"`.

Use the version endpoints to audit which user or agent changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

### List versions

List paginated version metadata for a store, newest-first. Filter by `memory_id`, `operation` (`created`, `modified`, or `deleted`), `session_id`, `api_key_id`, or a `created_at_gte`/`created_at_lte` time range. The list response does not include the `content` body; fetch individual versions with `retrieve` when you need the full content.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions?memory_id=$mem_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  | jq -r '.data[] | "\(.id): \(.operation)"'
```

### Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions/$version_id" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01"
```

### Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests. Redact hard clears `content`, `content_sha256`, `content_size_bytes`, and `path`; all other fields, including the actor and timestamps, are preserved.

curlPythonTypeScriptC#GoJavaPHPRuby

```shiki
curl -fsS -X POST "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions/$version_id/redact" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: managed-agents-2026-04-01" \
  -H "content-type: application/json" \
  -d '{}'
```

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
