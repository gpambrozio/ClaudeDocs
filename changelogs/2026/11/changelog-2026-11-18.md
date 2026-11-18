# [Claude docs changes for November 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/13dbab2270e966b553bc6694befa402c7dd6504e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/13dbab2270e966b553bc6694befa402c7dd6504e)]

## Executive Summary
- Claude Code 2.1.327 adds `/status` diagnostics for broken config, `claude mcp add-json <name> -` (read JSON from stdin), the `attributionProject` setting, and many stricter permission and path checks.
- New docs explain how to run one self-hosted sandbox per session (Helm chart, spawn script or SDK poller), and the self-hosted workers, memory and reference pages were substantially reworked.
- Auto mode documentation now covers fixing server-side classifier "policy" denials, and the permissions and mods docs clarify what a user-installed mod can and cannot override.
- Linked billing (OAuth apps) gains endpoints to read a customer's link status and to unlink a customer through the Claude API.
- Claude Platform on AWS docs add a "Request higher limits" flow, spend-cap details, and a rewritten Bedrock migration comparison.

## New Claude Code versions

### [2.1.327](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/versions/2.1.327.md)

#### New features

* `/status` now lists broken agent, skill, command and output-style files, keybinding errors, an unavailable sandbox, ignored permission settings and hook matchers that never match
* `claude mcp add-json <name> -` reads the server JSON from stdin, keeping tokens off the command line
* New `attributionProject` setting names a session's billing group for Claude apps gateways that set `admin.billing_group_tag`
* `x-claude-code-managed-settings-checksum` added to gateway hint headers
* `/tui classic` names the non-fullscreen renderer (`/tui default` still works)
* `/config` shows a note when other settings override a row; confirmation added before `/install-github-app` changes a repository
* VS Code: "Claude Code: Add to Chat" in the Explorer right-click menu

#### Existing feature improvements

* Faster first Bash command (shell start-up files may run before approval; disable with `CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1`)
* Claude is told not to commit files that likely contain secrets
* Transcript search now finds text in edits and written files
* Improved Windows startup and PowerShell tool speed
* Redesigned `/mcp` server pages, narrow-terminal layouts, and unnumbered lists outside screen reader mode
* Resuming very long sessions retries a truncated transcript read; subagent progress summaries on Bedrock/Vertex/Foundry use far fewer tokens
* Stricter permissions: `ExitWorktree` asks before removing a worktree with possibly unsaved work; symlink path checks refuse more links; `permissions.blockReadsOutsideWorkingDirectories` covers more Bash commands; auto mode ignores more run-any-package allow rules (e.g. `Bash(pnpm dlx *)`); PowerShell asks before one more command; arrow keys on permission prompts stop at No
* `claude mcp add --scope project` stops instead of overwriting a `.mcp.json` with top-level servers and no `mcpServers` key
* Auto mode warns that an upcoming release removes the billed classifier fallback
* Code Mode no longer refuses to start when a mod hooks tool calls
* Artifact tool/approval behavior tightened for organizations requiring approval per artifact
* WebFetch refuses URLs over 2,000 characters; only the first 100 `@` mentions are looked up as files

#### Major bug fixes

* `claude mcp add/remove` no longer deletes other top-level keys in `.mcp.json`
* `/export` no longer overwrites an existing file without asking
* Remote Control worktree mode no longer deletes a running session's git-ignored files (e.g. `.env`)
* Self-hosted runner no longer deletes a directory named by `GIT_CONFIG_GLOBAL`
* Fixed lost messages/tasks and wrong state on resume in headless, cloud and remote sessions
* Fixed `--agents` agents lost after plugins load, and plugin agents dropped on `--resume`
* Fixed startup failures with bare `host:port` `https_proxy` and `claude -p` hangs when model settings fetch stalls
* Fixed remote MCP servers staying disconnected after long outages (now retried in background for about a day)
* Fixed Grep paging with `head_limit`/`offset`, Read on notebooks with unknown output types, and NotebookEdit removing the final newline
* Fixed several hooks failing silently, and `/hooks` omitting hooks from `--settings`

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Array settings such as `permissions.allow`/`deny` merge entries from lower-precedence settings; link added to the lists-merge rules. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/admin-setup.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Clarified that `permissions.deny` blocks matching calls before the classifier runs. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/auto-mode-config.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/auto-mode-config#where-the-classifier-reads-configuration)]
* New section on fixing policy denials (`Destructive or Unwanted Actions`, `Unauthorized Access`, `Undermining Oversight`, `Unsanctioned Communication`): inspect under `/permissions` → Recently blocked, then allow once, add `autoMode.environment`, or add an `autoMode.allow` entry. [[lines 412-428](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/auto-mode-config.md?plain=1#L412-L428)] [[Source](https://code.claude.com/docs/en/auto-mode-config#fix-destructive-or-unwanted-actions-and-other-policy-denials)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Added "Create Public Threads" to the listed Discord permissions. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/channels.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* New `isolatePeerMachines` setting requires your approval before `SendMessage` reaches a session beyond this machine. [[lines 149-272](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/cross-session-messaging.md?plain=1#L149-L272)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#message-sessions-on-other-machines)]
* To get replies from another machine, connect your session to Remote Control before sending, otherwise the message has no reply address. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/cross-session-messaging.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#replies-from-other-machines-and-cloud-sessions)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Troubleshooting entry: local sessions fail when the desktop app's bundled Claude Code is newer than the org's `requiredMaximumVersion`. [[line 2359](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/desktop.md?plain=1#L2359)] [[Source](https://code.claude.com/docs/en/desktop#claude-code-is-newer-than-the-maximum-version-allowed-by-your-organization)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same `requiredMaximumVersion` troubleshooting entry added. [[line 2359](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/desktop-changelog.md?plain=1#L2359)] [[Source](https://code.claude.com/docs/en/desktop-changelog#claude-code-is-newer-than-the-maximum-version-allowed-by-your-organization)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* PermissionDenied input now documents the `reason` field and its typical values (classifier policy name, no verdict, classifier unavailable). [[line 2531](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/hooks.md?plain=1#L2531)] [[Source](https://code.claude.com/docs/en/hooks#permissiondenied-input)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Connector tools set to `ask` by the org prompt on every call, even in `acceptEdits`, `auto` and `bypassPermissions`. [[line 1407](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/mcp.md?plain=1#L1407)] [[Source](https://code.claude.com/docs/en/mcp#organization-controls-on-connector-tools)]
* MCP servers can mark a tool as requiring explicit approval with `_meta["anthropic/requiresUserInteraction"]: true`; no "don't ask again" is offered. [[lines 1610-1618](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/mcp.md?plain=1#L1610-L1618)] [[Source](https://code.claude.com/docs/en/mcp#require-approval-for-a-specific-tool)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `classifier_category` attribute on the tool decision event now documented with when it is present and version caveats (before v2.1.302 / v2.1.323). [[lines 1019-1024](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/monitoring-usage.md?plain=1#L1019-L1024)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Tip: when telling Claude a blocked action is allowed, name the action and its specifics (e.g. the branch of a force push). [[line 550](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permission-modes.md?plain=1#L550)] [[Source](https://code.claude.com/docs/en/permission-modes#approvals-you-state-in-conversation)]
* The classifier's block reason is now usually a policy or rule name in brackets. [[line 596](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permission-modes.md?plain=1#L596)] [[Source](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Permission prompt comment field: `Tab` closes it without answering; press again to send the text. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt)]
* `dontAsk` mode note: an installed mod can still approve some calls in certain setups. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* Org `ask` setting on a claude.ai connector tool overrides local allow rules. [[line 588](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md?plain=1#L588)] [[Source](https://code.claude.com/docs/en/permissions#mcp)]
* Precedence section expanded: what a user-installed mod using `tool.check` can approve or skip (ask rules, PreToolUse hooks, auto mode classifier) in setups without managed settings. [[lines 636-650](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md?plain=1#L636-L650)] [[Source](https://code.claude.com/docs/en/permissions#precedence-among-rules-hooks-and-mods)]
* `/add-dir` with a subdirectory of the primary working directory loads its skills, commands and subagents mid-session. [[line 722](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/permissions.md?plain=1#L722)] [[Source](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* Deleting a plugin's data also removes MCPB bundle files extracted into `~/.claude/plugins/mcpb/` (v2.1.326+). [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/cli-reference.md?plain=1#L182)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#what-an-uninstall-deletes-and-keeps)]

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* Rewrote the default-behavior section: what the built-in guard blocks a user's mod from rewriting, that deny/ask rules and blocked PreToolUse hooks hold when a mod approves a call, and that a mod's own `$.fs`, `$.process`, `$.tool.call` and `$.mcp.call` calls can skip checks. [[lines 60-100](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/admin.md?plain=1#L60-L100)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-what-happens-by-default)]
* `$.mcp.call` added to the API table (no permission prompt). [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/admin.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#review-what-a-mod-can-do)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* New "Hide command text from Claude" section: return `{ text, isTextDisplayOnly: true }` (v2.1.326+). [[lines 33-40](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/api.md?plain=1#L33-L40)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#add-a-command)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `$.tool` gains `check`; `$.agent` gains `call` and `limits` (v2.1.326+) and `list()` details. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/plugins/mods/reference.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#mods-api-methods)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `requiredMaximumVersion`: auto-updates and `claude update` skip versions above the ceiling (recovery commands still work), and the desktop app's bundled copy can exceed it and block local sessions. [[lines 5452-5454](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/claude-code/settings-reference.md?plain=1#L5452-L5454)] [[Source](https://code.claude.com/docs/en/settings-reference#requiredmaximumversion)]

-----

## API changes

### New Documents

#### [api/beta/organization/claude_tag/bundles/update](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/beta/organization/claude_tag/bundles/update.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles/update)]

Reference for `POST /v1/organizations/claude_tag/bundles/{bundle_id}` (Update Bundle). It partially updates a Claude Tag Bundle's `instructions`; null or an empty string clears them. Includes path parameters, headers and examples.

#### [managed-agents/self-hosted-sandboxes-per-session](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/managed-agents/self-hosted-sandboxes-per-session.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-per-session)]

"Run one sandbox per session": how to give each Managed Agents session its own self-hosted sandbox using the Helm chart on Kubernetes, a spawn script (called once per claimed work item), or the SDK poller. Split out from the workers page.

### Changed documents

#### [api/beta/organization/claude_tag](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/beta/organization/claude_tag.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag)]

* New Update Bundle endpoint, and a new `instructions` field on Bundles (added to every session that can use the Bundle). [[lines 4505-4990](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/beta/organization/claude_tag.md?plain=1#L4505-L4990)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag#returns)]
* New error details `bundle_attachment_not_supported` and `bundle_on_call`. [[lines 20-35](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/beta/organization/claude_tag.md?plain=1#L20-L35)] [[Source](https://platform.claude.com/docs/en/api/beta/organization/claude_tag#beta-bundle-attachment-not-supported-error-details)]
* New `user-profiles-billing-2026-10-01` beta header value on the endpoints.

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Linked billing is not available on Claude Platform on AWS. [[line 592](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L592)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#features-not-supported)]
* New step-by-step "Request higher limits" flow in the Claude Console, including the required IAM actions, the Start tier and Custom tier badge, and ZDR/CMEK exceptions. [[lines 840-880](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L840-L880)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#rate-limits-and-quotas)]
* Tier spend caps (HTTP 429 when reached) and CloudTrail coverage limits documented. [[lines 888-909](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L888-L909)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#spend-limits)]
* Available Console pages table and Bedrock migration comparison table reworked. [[lines 811-833](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L811-L833)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#available-pages)]

#### [build-with-claude/handling-stop-reasons](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* New "When a server tool is still waiting" section: a `tool_use` response may contain a `server_tool_use`/`mcp_tool_use` block with no result when server and client tools are called in parallel. [[line 1461](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L1461)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#when-a-server-tool-is-still-waiting)]
* Java tool-use example rewritten using the Java SDK. [[lines 1365-1394](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L1365-L1394)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#tool_use)]

#### [manage-claude/oauth-apps/organization-billing-connections](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/oauth-apps/organization-billing-connections.md) [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections)]

* New "Reading a customer's link status" section: request the user profile with `oauth_app_id` and the `user-profiles-search-2026-08-30` beta header to get `connection_status` (`connected`, `disconnected`, `not_connected`). [[line 1375](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/oauth-apps/organization-billing-connections.md?plain=1#L1375)] [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#reading-a-customers-link-status)]
* New `POST /v1/user_profiles/{id}/unlink` alternative to the revocation endpoint, with a comparison table and 503 retry guidance. [[lines 1656-1678](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/oauth-apps/organization-billing-connections.md?plain=1#L1656-L1678)] [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#unlinking-a-customer)]
* Troubleshooting: new connections can take about 10 seconds to work, customer org must be eligible, and customers manage links on the Linked platforms page. [[lines 1706-1745](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/oauth-apps/organization-billing-connections.md?plain=1#L1706-L1745)] [[Source](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections#expected-errors)]

#### [manage-claude/usage-cost-api](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* Marked as the legacy Admin API endpoints (new integrations should use the Usage and Cost Analytics API); added an authentication section and a table of which API and key each Claude product uses. [[lines 6-50](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L6-L50)] [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api#first-request)]

#### [managed-agents/self-hosted-sandboxes-workers](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/managed-agents/self-hosted-sandboxes-workers.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers)]

* Substantially restructured; the per-session sandbox content moved to the new per-session page. Related pages (`self-hosted-sandboxes`, `-memory`, `-reference`, `-operations`, `-custom-tools`, `-security`) were also revised to match.

#### [api/beta/messages (and SDK variants)](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* Beta Messages reference additions (about 84 lines) mirrored across the Python, CLI, Java, Go, C#, Ruby and PHP SDK pages, along with beta webhooks, sessions, environments and memory store references.

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/13dbab2270e966b553bc6694befa402c7dd6504e/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* The Compliance API reference, `compliance/activities` and `compliance/activities/list` pages were heavily regenerated (largely schema and listing churn).
