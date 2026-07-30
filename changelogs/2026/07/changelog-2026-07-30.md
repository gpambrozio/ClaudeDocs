# [Claude docs changes for July 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/88cb1cbbb36721ab0775587abd485cde9e8d20fa) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/88cb1cbbb36721ab0775587abd485cde9e8d20fa)]

## Executive Summary
- Desktop app: Claude can now work across your other Code tab sessions — listing them, reading what they've been doing, sending messages between them, and renaming or archiving them (with your approval) — a new "Work across sessions" capability.
- A new configuration warning is documented: permission rules written against `Write`, `NotebookEdit`, `MultiEdit`, or `Glob` paths are accepted but silently ignored, since file permission checks only consult `Edit`/`Read` path rules.
- Routines' branch-push safety model changed: instead of a manual "Allow unrestricted branch pushes" toggle, Claude Code now automatically rejects pushes to non-`claude/` branches that are protected on GitHub, have an open PR from someone else, or carry another author's commits.
- JetBrains plugin gains a **Diff tool** setting in `/config` to choose between the IDE diff viewer and the terminal.
- Task tracking: todos are now explicitly deleted by setting `status: "deleted"` in a `TaskUpdate` call, rather than being auto-removed once a task group completes.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/todo-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/agent-sdk/todo-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking)]

* Todo removal is now explicit: Claude deletes a todo it no longer needs by setting `status: "deleted"` in a `TaskUpdate` call, rather than todos being auto-removed once their group completes. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/agent-sdk/todo-tracking.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking#todo-lifecycle)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New "Work across sessions" capability: Claude can list your other Code tab sessions, read what each has been doing, and send messages between them, plus rename or archive a session on your behalf. It only sees local, SSH, and WSL desktop sessions (not cloud, terminal CLI, or VS Code sessions), skips the session you're asking from, and by default considers your 20 most recently active, non-archived sessions. Claude always asks before archiving a session, can't message into or out of an unwatched session such as a scheduled-task run, and quotes/attributes incoming messages so you can tell where they came from. [[lines 306-319](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop.md?plain=1#L306-L319)] [[Source](https://code.claude.com/docs/en/desktop#work-across-sessions)]
* Bypass permissions mode now also always asks first for certain desktop actions, such as archiving a session via the new cross-session capability. [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]
* Clarifies that "Agent teams" specifically means coordinated teams, where Claude acts as team lead and assigns tasks to teammates from a shared task list; notes Claude can also message and manage other sessions directly instead. [[line 787](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop.md?plain=1#L787)] [[Source](https://code.claude.com/docs/en/desktop#whats-not-available-in-desktop)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Notes that a scheduled-task session can't send or receive cross-session messages, unlike a regular Desktop session. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#how-scheduled-tasks-run)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Clarifies that code intelligence plugins require you to install the language server binary yourself; the plugin doesn't install it for you. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/discover-plugins.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/discover-plugins#code-intelligence)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New documented configuration warning, "`... is not matched by file permission checks`": raised for a `Write`, `NotebookEdit`, `MultiEdit`, or `Glob` permission rule with a path, since those checks only consult `Edit`/`Read` path rules; the rule is kept but never applied. Covers the fix (use `Edit`/`Read` instead), the `--allowedTools` exception for `Glob`, and that it logs to the debug log instead of stderr in background sessions or JSON output modes. [[lines 1502-1516](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/errors.md?plain=1#L1502-L1516)] [[Source](https://code.claude.com/docs/en/errors#is-not-matched-by-file-permission-checks)]

#### [jetbrains](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* New **Diff tool** setting in `/config`, letting you switch between showing diffs in the IDE viewer (`auto`) or the terminal (`terminal`); only appears when connected to the IDE. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/jetbrains.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/jetbrains#features)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Documents the [`switchModelsOnFlag`](https://code.claude.com/docs/en/settings) settings-file option as an alternative to the `/config` toggle for controlling automatic model switching on flagged requests. [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/model-config.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/model-config#ask-before-switching)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarifies that legacy `MultiEdit(path)` rules are also silently unmatched by file permission checks (only `Edit`/`Read` path rules apply), and that a `Glob` rule passed via `--allowedTools` is now accepted without a startup warning. [[line 227](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/permissions.md?plain=1#L227)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Branch-push policy changed: routines still always push freely to `claude/`-prefixed branches, but a push directed at any other branch is now checked automatically and rejected if that branch is protected on GitHub, has an open pull request from someone else, or carries commits authored by someone other than you — replacing the previous "Allow unrestricted branch pushes" permission toggle, and the routine creation form's Permissions tab has been removed accordingly. [[lines 291-294](https://github.com/gpambrozio/ClaudeDocs/blob/88cb1cbbb36721ab0775587abd485cde9e8d20fa/docs-md/claude-code/routines.md?plain=1#L291-L294)] [[Source](https://code.claude.com/docs/en/routines#repositories-and-branch-permissions)]
