# [Claude docs changes for April 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/54e7e97d77444bef93961ba74a49f0bfca764bdb) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/54e7e97d77444bef93961ba74a49f0bfca764bdb)]

## Executive Summary
- The Desktop app's "Schedule" page has been renamed to "Routines" with a unified interface for both local and remote tasks, including improved task history with skip-reason tooltips and a new one-time task capability via natural language
- SSH sessions in Desktop now automatically install Claude Code on the remote machine — manual pre-installation is no longer required
- The `/claude-api` skill gained two new subcommands: `migrate` for upgrading existing code to a newer Claude model, and `managed-agents-onboard` for an interactive walkthrough to create a new Managed Agent
- Terminal theming gained a comprehensive color token reference documenting all customizable tokens (text, status, diff rendering, subagent colors, etc.)
- The Managed Agents memory store limits table was removed; specific values are no longer published in the docs

-----

## Claude Code changes

### Changed documents

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* The `/claude-api` skill now accepts two optional subcommands: `migrate` (scans files and updates model IDs, thinking config, and other version-specific parameters to a target model) and `managed-agents-onboard` (interactive walkthrough that creates a new Managed Agent from scratch). [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/commands.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/commands)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* The Desktop app now has three named tabs: **Chat**, **Cowork**, and **Code**; the page now explicitly describes itself as the Code tab reference. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/desktop)]
* Windows setup now states Git for Windows must be installed before the Code tab works, and the app requires a restart after installing it. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/desktop)]
* SSH sessions no longer require Claude Code to be pre-installed on the remote machine — Desktop installs it automatically on first connect. [[line 476](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L476)] [[Source](https://code.claude.com/docs/en/desktop#ssh-sessions)]
* The preview pane and file pane now support **video** files in addition to HTML, PDFs, and images. [[lines 77](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* Auto mode availability details moved into a dedicated note block; the permission modes table now links to an `#auto-mode-availability` anchor rather than inlining all requirements. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]
* `--allowedTools` / `--disallowedTools` CLI comparison entry updated: now documented as having no per-session equivalent but notes that permission rules in settings files still apply. [[line 572](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L572)] [[Source](https://code.claude.com/docs/en/desktop#cli-flag-equivalents)]
* Managed settings clarification: a file deployed to disk applies to Desktop sessions, but settings pushed remotely through the admin console currently reach CLI and IDE only — Desktop deployments should use MDM or admin console controls. [[line 524](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L524)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]
* A new **Customize** sidebar link is mentioned as the single place to manage connectors, skills, and plugins. [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop.md?plain=1#L295)] [[Source](https://code.claude.com/docs/en/desktop#extend-claude-code)]

#### [desktop-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* SSH environment description updated: Desktop now automatically installs Claude Code on the remote machine the first time you connect (previously required manual installation). [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-quickstart.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#start-your-first-session)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* The **Schedule** page in the Desktop sidebar has been renamed to **Routines**; "New task" / "New local task" buttons are now "New routine" / "Local". [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L28)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)]
* The page now explicitly describes both local scheduled tasks and remote routines as accessible from the same Routines page. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]
* Task creation form field names changed: "Prompt" → "Instructions", "Frequency" → "Schedule". A project folder is now required before saving a task. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)]
* Natural language task creation now explicitly supports one-time tasks (e.g. "remind me at 3pm tomorrow to check the deploy"), which disable themselves after firing. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)]
* Task history now shows skip reasons on hover (computer asleep, previous run still in progress, other tasks running) and a "Show more" button to load older entries. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)]
* "Toggle repeats" renamed to **Status** toggle (Active / Paused). Task deletion is now only available via the Delete button in the UI, no longer via conversational commands. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* The create routine form now has a **Permissions** tab alongside the Connectors tab; the "Allow unrestricted branch pushes" option has moved from the repository selector to this Permissions tab. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/routines.md?plain=1#L84)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]
* Desktop app navigation for creating remote routines updated: now "Routines" in sidebar → "New routine" → "Remote" (previously "Schedule" → "New task" → "New remote task"). The separate "Create from the Desktop app" section was removed. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/routines.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/routines#create-a-routine)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* A comprehensive **color token reference** was added documenting all theme override tokens, including: text and accent colors (`claude`, `text`, `inactive`, `subtle`, `permission`, `remember`), status colors (`success`, `error`, `warning`, `merged`), input box and mode indicators (`promptBorder`, `planMode`, `autoAccept`, `bashBorder`, `ide`, `fastMode`), diff rendering tokens (`diffAdded`, `diffRemoved`, and word/dimmed variants), fullscreen mode tokens (`userMessageBackground`, `selectionBg`), and shimmer variants and per-subagent color tokens. [[lines 133-220](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/claude-code/terminal-config.md?plain=1#L133-L220)] [[Source](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)]

-----

## API changes

### Changed documents

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* The specific limits table for memory stores (stores per org, memories per store, storage size, version history, etc.) was removed. The Limits section now states only that "Default capacity and rate limits apply" during beta. [[line 281](https://github.com/gpambrozio/ClaudeDocs/blob/54e7e97d77444bef93961ba74a49f0bfca764bdb/docs-md/api/managed-agents/memory.md?plain=1#L281)] [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]
