# Adding files

Copy page

You can provide files to your agent by uploading them via the Files API and mounting them in the session's container.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Uploading files

First, upload a file using the [Files API](build-with-claude/files.md):

curl

```shiki
file=$(curl --fail-with-body -sS "${auth[@]}" \
  "${base_url}/files" \
  -F file=@data.csv)
file_id=$(jq -er '.id' <<<"${file}")
printf 'File ID: %s\n' "${file_id}"
```

## Mounting files in a session

Mount uploaded files into the container by adding them to the `resources` array when creating a session:

The `mount_path` is optional, but make sure the uploaded file has a descriptive name so the agent knows what it is looking for.

curl

```shiki
session=$(
  jq -n \
    --arg agent_id "${agent_id}" \
    --arg environment_id "${environment_id}" \
    --arg file_id "${file_id}" \
    '{
      agent: $agent_id,
      environment_id: $environment_id,
      resources: [
        {
          type: "file",
          file_id: $file_id,
          mount_path: "/workspace/data.csv"
        }
      ]
    }' | curl --fail-with-body -sS "${auth[@]}" "${base_url}/sessions" --json @-
)
session_id=$(jq -er '.id' <<<"${session}")
```

A new `file_id` will be created that references the instance of the file in the session. These copies do not count against your [storage limits](build-with-claude/files.md).

## Multiple files

Mount multiple files by adding entries to the `resources` array:

curl

```shiki
"resources": [
  { "type": "file", "file_id": "file_abc123", "mount_path": "/workspace/data.csv" },
  { "type": "file", "file_id": "file_def456", "mount_path": "/workspace/config.json" },
  { "type": "file", "file_id": "file_ghi789", "mount_path": "/workspace/src/main.py" }
]
```

A maximum of 100 files is supported per session.

## Managing files on a running session

You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.

curl

```shiki
resource=$(
  jq -n --arg file_id "${file_id}" '{type: "file", file_id: $file_id}' \
    | curl --fail-with-body -sS "${auth[@]}" \
        "${base_url}/sessions/${session_id}/resources" --json @-
)
resource_id=$(jq -er '.id' <<<"${resource}")
printf '%s\n' "${resource_id}"  # "sesrsc_01ABC..."
```

List all resources on a session with `resources.list`. To remove a file, call `resources.delete` with the resource ID:

curl

```shiki
curl --fail-with-body -sS "${auth[@]}" \
  "${base_url}/sessions/${session_id}/resources" \
  | jq -r '.data[] | "\(.id) \(.type)"'

curl --fail-with-body -sS "${auth[@]}" -X DELETE \
  "${base_url}/sessions/${session_id}/resources/${resource_id}" >/dev/null
```

## Listing and downloading session files

Use the [Files API](build-with-claude/files.md) to list files scoped to a session and download them.

curl

```shiki
# List files associated with a session
curl -fsSL "https://api.anthropic.com/v1/files?scope_id=sess_abc123" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"

# Download a file
curl -fsSL "https://api.anthropic.com/v1/files/$FILE_ID/content" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -o output.txt
```

## Supported file types

The agent can work with any file type, including:

- Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, etc.)
- Data files (`.csv`, `.json`, `.xml`, `.yaml`)
- Documents (`.txt`, `.md`)
- Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
- Binary files - the agent can process these with appropriate tools

## File paths

Files mounted in the container are read-only copies. The agent can read them but cannot modify the original uploaded file. To work with modified versions, the agent writes to new paths within the container.

- Files are mounted at the exact path you specify
- Parent directories are created automatically
- Paths should be absolute (starting with `/`)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
