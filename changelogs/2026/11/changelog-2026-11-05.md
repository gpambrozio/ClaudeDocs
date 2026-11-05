# [Claude docs changes for November 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ae4013afc53035a974f590fa0cf2b9a460281ce8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ae4013afc53035a974f590fa0cf2b9a460281ce8)]

## Executive Summary
- New beta **IP allowlisting** guide: restrict where an organization's API keys and Enterprise sign-ins can be used from, with up to 1,000 IPv4/IPv6 addresses or CIDR ranges.
- New beta Admin API endpoint (`POST /v1/organizations/users/{user_id}/sign_out`) signs a Claude Enterprise member out of every browser and device without removing them.
- The Claude Code errors page now covers corrupted or empty `~/.claude.json` recovery, organization settings that must load before a session starts, and new Remote Control failure messages.
- The Desktop app can minimize the Terminal, Browser, and iOS Simulator panes, and has new guidance on scheduled-task sign-in expiry.
- Compliance API now covers Claude Tag (Slack) sessions. SDKs bumped to new minor versions, and the Ruby SDK now supports Microsoft Foundry.

## New Claude Code versions

No new version files in this commit.

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added a `config_file_invalid` termination reason for when Claude Code refuses to start because `~/.claude.json` isn't valid JSON.

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* `ANTHROPIC_BEDROCK_SERVICE_TIER` is now documented as applying to every Invoke API request except model access checks. Background sessions need it set in the `env` block of settings.
* The Mantle setup now requires setting your AWS region along with `CLAUDE_CODE_USE_MANTLE`.

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Clarified the `~/.claude/backups/` retention rules. The five newest copies are kept, and the last copy holding your configuration is deleted too once it is past the age cutoff. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/claude-directory.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]
* Backups are now listed as the copies you can restore `~/.claude.json` from. [[lines 287-288](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/claude-directory.md?plain=1#L287-L288)] [[Source](https://code.claude.com/docs/en/claude-directory#clear-local-data)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* Revised the GitHub access troubleshooting steps. If a repository can't be reached, ask Claude in the project conversation to start a new thread for the same work.

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New "Minimize a pane" section. Terminal, Browser, and iOS Simulator panes can be minimized, and then docked in the session details panel or floated in a chat corner. It requires Desktop v4.0.0 or later. [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop.md?plain=1#L226)] [[Source](https://code.claude.com/docs/en/desktop#minimize-a-pane)]
* Warning that scheduled tasks signed in with a Claude account may not run overnight, because the sign-in is renewed only while Desktop is running, connected, and signed in. It also adds steps to check when a task didn't finish. [[line 1296](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop.md?plain=1#L1296)] [[Source](https://code.claude.com/docs/en/desktop#keep-a-task-running-while-desktop-is-disconnected)]
* Clarified that a permission mode picked in a local session is remembered per folder. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Mirrors the Desktop changes above: pane minimizing, scheduled-task sign-in caveats, and the permission-mode note.

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* Clarified consent and permissions. Claude asks before controlling a device, and after you allow it, taps, typing, and screenshots run without prompts. Installing and launching the app (and opening URLs) still follows your permission mode, and access can be turned off entirely. [[lines 90-112](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L90-L112)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#how-sessions-manage-devices)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries for a corrupted `~/.claude.json` ("Configuration error in ~/.claude.json"), including the backup `cp` restore line, and for an empty config file with no backup. As of v2.1.318, non-interactive starts no longer silently continue with defaults. [[line 3270](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L3270)] [[Source](https://code.claude.com/docs/en/errors#settings-file-exceeds-the-2mib-limit)]
* New "Claude Code couldn't load your organization's settings" section. When Anthropic requires organization settings, sessions can't start until they load. It gives a fix for each failure cause. [[line 5942](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L5942)] [[Source](https://code.claude.com/docs/en/errors#claude-code-couldnt-load-your-organizations-settings)]
* New authentication warnings when `/logout` or a re-login can't remove the previous account or API key from the config file. [[line 1456](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L1456)] [[Source](https://code.claude.com/docs/en/errors#couldnt-save-your-login)]
* New tool error: a command approved before a restart was not run because the shell's directory couldn't be confirmed. [[line 4750](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L4750)] [[Source](https://code.claude.com/docs/en/errors#command-contains-an-invisible-character)]
* New "Make this change again later" notice when `~/.claude.json` couldn't be updated. [[line 6418](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L6418)] [[Source](https://code.claude.com/docs/en/errors#sandbox-mask-files-left-behind-at-write-deny-paths)]
* New image error for the 3000px dimension limit on many-image requests (use `/compact`), plus Remote Control "working folder not found" and "program file is gone" entries. [[line 2463](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/errors.md?plain=1#L2463)] [[Source](https://code.claude.com/docs/en/errors#image-was-too-large)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Bare mode doesn't run hooks passed through `--settings` or through the `hooks` of a plugin loaded by flag, so don't use bare mode for runs that need them.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Clarified that a mode picked in a local session outranks a project `defaultMode`, but a new session can still start in a `defaultMode` from user or managed settings. [[line 244](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/permission-modes.md?plain=1#L244)] [[Source](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)]
* Split the auto mode server-check version requirements. It is v2.1.278+ for `-p` and VS Code, and v2.1.281+ for the Agent SDK and desktop. [[lines 371-372](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/permission-modes.md?plain=1#L371-L372)] [[Source](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New troubleshooting for "working folder not found" and "The program file this Remote Control started from is gone". [[lines 501-515](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/remote-control.md?plain=1#L501-L515)] [[Source](https://code.claude.com/docs/en/remote-control#working-folder-not-found)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New `CLAUDE_RUNNER_SPAWN_REASON` variable (Claude Code v2.1.318+ on the orchestrator) tells your hook why a spawn request was sent. The section gives a table of values (`session_created`, `runner_lost`, `hook_failed`, ...) and what to check for each. [[lines 471-492](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L471-L492)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#find-out-why-a-spawn-request-was-sent)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* On Team or Enterprise claude.ai logins, Anthropic can require organization settings before a session starts. An expired sign-in or no cached settings then blocks startup. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/server-managed-settings.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]
* Clarified how failed loads are reported and how the CLI falls back to cached settings. [[line 229](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/server-managed-settings.md?plain=1#L229)] [[Source](https://code.claude.com/docs/en/server-managed-settings#invalid-entries-in-delivered-settings)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `permissions.defaultMode` is reworded as the default mode for new sessions.
* The settings-fetch startup key now notes that Anthropic can require the settings, which blocks startup on the fetch.

-----

## API changes

### New Documents

#### [manage-claude/ip-allowlist](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/manage-claude/ip-allowlist.md) [[Source](https://platform.claude.com/docs/en/manage-claude/ip-allowlist)]

New beta guide to IP allowlisting. Requests from addresses outside the list are refused (the Messages API returns a 403 `permission_error`). For Claude Platform organizations it covers the Console, core Claude API endpoints, Managed Agents endpoints, and the Admin and Compliance APIs. Claude Enterprise organizations have their own list covering the Claude apps, Claude Code with account sign-in, and more. The guide explains how to avoid locking admins out and lists limitations. It recommends combining the allowlist with short key expiration or Workload Identity Federation.

### Changed documents

#### [api/migration-2026-10-21 and api/beta/*, api/organization/*, api/compliance/*, api/user_profiles/* (SDK reference pages in all languages)](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/api/migration-2026-10-21.md) [[Source](https://platform.claude.com/docs/en/api/migration-2026-10-21)]

* About 470 generated API reference pages were regenerated across the language SDKs. This covers agents and versions, deployments, dreams, sessions, vaults, webhooks, Enterprise analytics, RBAC groups and roles, and spend limits.
* The TypeScript beta `webhooks` page is new (1,275 lines) and `webhooks/unwrap` was expanded.
* The Admin API reference gains the user sign-out operation, and `user_profiles` pages gained small additions.

#### [build-with-claude/claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* The Ruby SDK now supports Foundry natively through `Anthropic::FoundryClient`, replacing the earlier workaround. Foundry is now supported by all SDKs. Java examples are updated to 3.5.0.

#### [cli-sdks-libraries/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* SDK versions bumped: ant CLI 2.6.0, Python 2.5.0, TypeScript 1.5.0, C# 13.5.0, Go 2.6.0, Java 3.5.0, PHP 1.5.0, Ruby 2.5.0.

#### [manage-claude/compliance-sessions](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/manage-claude/compliance-sessions.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-sessions)]

* Remote session endpoints now also return Claude Tag sessions started in Slack, with a second `product_surface` value.
* Documented that Claude Tag transcripts have no default retention period and are deleted when the channel is removed, the channel is deleted in Slack, or similar events occur. Export any transcript you need to keep first.

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* New "Sign a member out everywhere" section for the beta `POST /v1/organizations/users/{user_id}/sign_out` endpoint. It ends sessions, trusted devices, and OAuth tokens without removing the member, and is useful for lost devices and security incidents.

#### [manage-claude/authentication](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/manage-claude/authentication.md) [[Source](https://platform.claude.com/docs/en/manage-claude/authentication)]

* Mostly wording and code-sample cleanups. It also fixes the workspace-key replacement link to point to Workload Identity Federation.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a November 5, 2026 entry announcing IP allowlisting (beta) and the beta Admin API member sign-out endpoint, which needs the `admin-user-sign-out-2026-10-08` beta header. [[lines 5-9](https://github.com/gpambrozio/ClaudeDocs/blob/ae4013afc53035a974f590fa0cf2b9a460281ce8/docs-md/api/release-notes/overview.md?plain=1#L5-L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#overview)]
