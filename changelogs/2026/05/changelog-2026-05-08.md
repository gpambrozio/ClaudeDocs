# [Claude docs changes for May 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ee8a747) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ee8a747)]

## Executive Summary
- Claude Code 2.1.133 adds hooks access to the active effort level via `effort.level` JSON and `$CLAUDE_EFFORT` env var, enabling hooks to react to the current reasoning effort setting
- New `worktree.baseRef` setting lets users control whether new worktrees branch from `origin/<default>` or local `HEAD`, with a notable behavior change: `EnterWorktree` now defaults back to `origin/<default>`
- C# SDK gains full webhook support with `BetaWebhooks` helpers for verifying signatures and parsing all session and vault event payloads
- Multiple significant bug fixes in 2.1.133, including parallel sessions losing credentials after token refresh races and subagents failing to discover skills

## New Claude Code versions

### [2.1.133](https://github.com/gpambrozio/ClaudeDocs/blob/ee8a747/versions/2.1.133.md)

#### New features

* Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it had been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
* Added `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) for specifying custom bubblewrap and socat binary locations
* Added `parentSettingsBehavior` admin-tier key (`'first-wins' | 'merge'`) to let admins opt SDK `managedSettings` (parent tier) into the policy merge
* Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable; Bash tool commands can also read `$CLAUDE_EFFORT`

#### Existing feature improvements

* Improved focus mode behavior
* Improved memory usage by releasing warm-spare background workers under memory pressure
* `claude --help` now lists `--remote-control` alongside `--remote-control-session-name-prefix`

#### Major bug fixes

* Fixed parallel sessions all dead-ending at 401 after a refresh-token race wiped shared credentials
* Fixed `Edit`/`Write` allow rules scoped to a drive root (`C:\`) or POSIX `/` matching incorrectly and always prompting
* Fixed an unhandled rejection (`ECOMPROMISED`) when a history or session-log file lock is compromised by clock skew or slow disk
* Fixed pressing Esc during conversation compaction showing a spurious "Error compacting conversation" notification
* Fixed `HTTP(S)_PROXY` / `NO_PROXY` / mTLS not being respected for the full MCP OAuth flow including discovery, dynamic client registration, token exchange, and token refresh
* Fixed Read/Write/Edit being denied on mapped network drives passed via `--add-dir` / SDK `additionalDirectories`
* Fixed Remote Control stop/interrupt from claude.ai not fully canceling the CLI session the same way local Esc does, causing queued messages to never advance after interrupting a stuck tool or prompt
* Fixed `/effort` in one session unexpectedly changing the effort level of other concurrent sessions, and a related issue where an IDE effort change could be silently dropped
* Fixed subagents not discovering project, user, or plugin skills via the Skill tool
* [VSCode] Fixed `claudeCode.claudeProcessWrapper` failing with "Unsupported platform" when the extension build doesn't bundle a Claude binary

-----

## Claude Code changes

### Changed documents

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/ee8a747/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Removed the inline installation UI snippet (platform tabs for Terminal/Desktop/VS Code/JetBrains, OS selector, and the `curl` install command) from the top of the overview page

-----

## API changes

### New Documents

#### [api/csharp/beta/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/ee8a747/docs-md/api/api/csharp/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/webhooks)]

New C# SDK reference page documenting the `BetaWebhooks` helpers for receiving and verifying webhook events. Covers the `unwrap` method for signature verification and payload parsing, and lists all supported `data.type` values for session lifecycle events (`session.created`, `session.running`, `session.idled`, etc.) and vault/credential events (`vault.created`, `vault_credential.refresh_failed`, etc.).

### Changed documents

#### [api/csharp/beta](https://github.com/gpambrozio/ClaudeDocs/blob/ee8a747/docs-md/api/api/csharp/beta.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta)]

* Added a new `BetaWebhooks` section with full C# class definitions for all webhook event types, including `BetaWebhookEvent`, `BetaWebhookEventData` (union type), `UnwrapWebhookEvent`, and the full set of session and vault/credential event data classes [[line 43927](https://github.com/gpambrozio/ClaudeDocs/blob/ee8a747/docs-md/api/api/csharp/beta.md?plain=1#L43927)] [[Source](https://platform.claude.com/docs/en/api/csharp/beta)]
