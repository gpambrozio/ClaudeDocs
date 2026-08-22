# Adding files

Copy page



You can provide files to your agent by uploading them through the Files API and mounting them in the session's sandbox.

##  Uploading files

First, upload a file using the [Files API](build-with-claude/files.md):

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
file = client.files.upload(file=Path("data.csv"))
print(f"File ID: {file.id}")
```

##  Mounting files in a session

Mount uploaded files into the sandbox by adding them to the `resources` array when creating a session:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
        {
            "type": "file",
            "file_id": file.id,
            "mount_path": "/data.csv",
        },
    ],
)
```

With the preceding `mount_path`, the agent reads the file at `/mnt/session/uploads/data.csv` (see [File paths](#file-paths)).

A new `file_id` is created that references the instance of the file in the session. These copies do not count against your [storage limits](build-with-claude/files.md).

##  Multiple files

Mount multiple files by adding entries to the `resources` array:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
resources = [
    {"type": "file", "file_id": "file_abc123", "mount_path": "/data.csv"},
    {"type": "file", "file_id": "file_def456", "mount_path": "/config.json"},
    {"type": "file", "file_id": "file_ghi789", "mount_path": "/src/main.py"},
]
```

A maximum of 500 files is supported per session.

##  Managing files on a running session

You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)
print(resource.id)  # "sesrsc_01ABC..."
```

List all resources on a session with `resources.list`. To remove a file, call `resources.delete` with the resource ID:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
listed = client.beta.sessions.resources.list(session.id)
for entry in listed.data:
    print(entry.id, entry.type)

client.beta.sessions.resources.delete(resource.id, session_id=session.id)
```

##  Listing and downloading session files

Use the [Files API](build-with-claude/files.md) to list files scoped to a session and download them. Files the agent writes to `/mnt/session/outputs/` appear in the list shortly after the agent finishes writing them, sometimes a few seconds after the session goes idle. If an output file you expect is missing, list again after a short delay; once it appears in the list, its upload has finished.

Filtering by `scope_id` requires the `managed-agents-2026-04-01` beta header, so the list examples use the `beta` files namespace and pass that header explicitly.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
# List files associated with a session
files = client.beta.files.list(
    scope_id="sesn_abc123",
    betas=["managed-agents-2026-04-01"],
)
for file in files:
    print(file.id, file.filename)

# Download a file
content = client.files.download(files.data[0].id)
content.write_to_file("output.txt")
```

##  Supported file types

The agent can work with any file type, including:

- Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, and others)
- Data files (`.csv`, `.json`, `.xml`, `.yaml`)
- Documents (`.txt`, `.md`)
- Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
- Binary files - the agent can process these with appropriate tools

##  File paths

- The path you specify is rooted under the session's uploads directory: a `mount_path` of `/data.csv` places the file at `/mnt/session/uploads/data.csv` in the sandbox
- If you omit `mount_path`, the file is placed at `/mnt/session/uploads/<file_id>`
- Parent directories are created automatically
- Paths should be absolute (starting with `/`)
- Files the agent writes to `/mnt/session/outputs/` become available through the Files API, scoped to the session; see [Listing and downloading session files](#listing-and-downloading-session-files)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
