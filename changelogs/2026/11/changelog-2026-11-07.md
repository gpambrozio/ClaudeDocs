# [Claude docs changes for November 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/255938ce92e54bae1a396e1ff699bc5a6c9fc873) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/255938ce92e54bae1a396e1ff699bc5a6c9fc873)]

## Executive Summary
- Deferred tool calls (`"defer"` hook) have new behavior when the tool is unavailable on resume: a new `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL` variable lets you drop the pending call (v2.1.319)
- `PostToolUse` hooks now run (with a 10-second limit) when a turn is ended with `Ctrl+Enter` during a tool call
- New `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS` variable lets `claude mcp add/remove` wait longer for the `~/.claude.json` lock
- Remote Control and Desktop can now be disabled via `remoteControlAtStartup: false` in managed settings (MDM policy)
- Cloud sessions no longer strictly require GitHub, and push notifications now work in cloud sessions

## New Claude Code versions

No new version files in this update.

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Clarified that on providers such as Amazon Bedrock and Google Cloud's Agent Platform, Claude Code doesn't pass the `display` thinking value. [[line 1352](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/agent-sdk/python.md?plain=1#L1352)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#thinkingconfig)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Same clarification about the `display` thinking value on Bedrock and Google Cloud's Agent Platform. [[line 5432](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5432)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#thinkingconfig)]

#### [auto-mode-classifier-billing](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/auto-mode-classifier-billing.md) [[Source](https://code.claude.com/docs/en/auto-mode-classifier-billing)]

* Rewrote the LLM gateway guidance with explicit requirements: forward the `anthropic-beta` header and `safeguards` body field together, and keep `safeguard_results` and tool-use IDs in responses. [[lines 28-33](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/auto-mode-classifier-billing.md?plain=1#L28-L33)] [[Source](https://code.claude.com/docs/en/auto-mode-classifier-billing#make-the-session-eligible)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Remote Control auto-connect is skipped when `remoteControlAtStartup` is `false` in managed settings; new "Keep sessions off your other devices" subsection with an MDM/managed-settings option. [[lines 548-559](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop.md?plain=1#L548-L559)] [[Source](https://code.claude.com/docs/en/desktop#control-which-sessions-appear-on-your-other-devices)]
* Features turned off via `browserExternalPageTools`, `disableMobileSimulatorTools`, or `disableBrowserExternalNavigation` in managed settings are covered in the managed-settings section. [[line 2016](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop.md?plain=1#L2016)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same Remote Control managed-settings and MDM changes as in the desktop page. [[lines 548-559](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop-changelog.md?plain=1#L548-L559)] [[Source](https://code.claude.com/docs/en/desktop-changelog#control-which-sessions-appear-on-your-other-devices)]

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* New section on minimizing or closing the simulator pane: Claude can still use the device, and clicking **iOS Simulator** in the title bar shows it again. [[lines 85-91](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L85-L91)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#minimize-or-close-the-simulator-pane)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS`: how long commands like `claude mcp add` wait for the `~/.claude.json` lock. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/env-vars.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL`: drops a deferred tool call whose tool is unavailable when resuming with `-p`. [[line 277](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/env-vars.md?plain=1#L277)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `MCP_PROTOCOL_NEGOTIATION` description updated (`legacy` keeps servers on the earlier handshake, `auto` probes). [[line 487](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/env-vars.md?plain=1#L487)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* "MCP server was not saved or removed" now explains lock contention from other Claude Code processes (10-20 second wait) and the fix via `CLAUDE_CODE_CONFIG_LOCK_WAIT_MS`; notes the behavior before v2.1.318. [[lines 3562-3579](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/errors.md?plain=1#L3562-L3579)] [[Source](https://code.claude.com/docs/en/errors#mcp-server-was-not-saved-or-removed)]
* Noted that a "file was not found" reason means the server may still be configured. [[line 3585](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/errors.md?plain=1#L3585)] [[Source](https://code.claude.com/docs/en/errors#mcp-server-may-not-have-been-saved-or-removed)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `"defer"` is honored only with `-p` and a single tool call; it is ignored with a warning in interactive sessions or with several tool calls. [[lines 2062-2068](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/hooks.md?plain=1#L2062-L2068)] [[Source](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)]
* New "Resume when a deferred tool is unavailable" section: the `tool_deferred_unavailable` stop reason, exit codes, and dropping the call with `CLAUDE_CODE_DROP_UNAVAILABLE_DEFERRED_TOOL=1`. Before v2.1.319, a prompt dropped the call. [[lines 2101-2114](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/hooks.md?plain=1#L2101-L2114)] [[Source](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)]
* New "PostToolUse after an interrupt" section: how `Ctrl+Enter`, `Enter` and `Esc` affect `PostToolUse` hooks. Hooks get 10 seconds after `Ctrl+Enter`, and `async: true` is recommended for longer ones. [[lines 2229-2240](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/hooks.md?plain=1#L2229-L2240)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-after-an-interrupt)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Tool counts in a cloud session" section explaining why a count like `3 of 13 tools available` appears (deny rules, names over 128 characters, `_meta.ui.visibility`). [[lines 305-314](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/mcp.md?plain=1#L305-L314)] [[Source](https://code.claude.com/docs/en/mcp#tool-counts-in-a-cloud-session)]
* Reorganized the runtime and protocol negotiation notes. With `MCP_PROTOCOL_NEGOTIATION` unset, Claude Code can skip asking a stdio server for 7 days. [[lines 358-360](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/mcp.md?plain=1#L358-L360)] [[Source](https://code.claude.com/docs/en/mcp#mcp-client-runtimes)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Documented two new warnings shown when the `NODE_EXTRA_CA_CERTS` file can only be partly read or not at all. [[lines 88-94](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/network-config.md?plain=1#L88-L94)] [[Source](https://code.claude.com/docs/en/network-config#custom-ca-certificates)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Updated the auto-mode classifier troubleshooting steps. Use `curl https://example.com` as the test command, and a `Disabled` result now suggests checking permission rules. [[lines 430-436](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/permission-modes.md?plain=1#L430-L436)] [[Source](https://code.claude.com/docs/en/permission-modes#check-which-model-the-classifier-used)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* New "Validate a manifest file" section: how `claude plugin validate` decides whether a file is a marketplace or a plugin manifest. [[lines 630-639](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/plugins/cli-reference.md?plain=1#L630-L639)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#validate-a-manifest-file)]

#### [plugins/marketplace-reference](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/plugins/marketplace-reference.md) [[Source](https://code.claude.com/docs/en/plugins/marketplace-reference)]

* Name the file `marketplace.json` to have it validated as a marketplace. [[line 454](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/plugins/marketplace-reference.md?plain=1#L454)] [[Source](https://code.claude.com/docs/en/plugins/marketplace-reference#validation-messages)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added guidance for the `Remote Control isn't connected.` dialog in `/remote-control`. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/remote-control.md?plain=1#L146)] [[Source](https://code.claude.com/docs/en/remote-control#check-connection-status)]

#### [sandbox-environments](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

* Cloud session requirements reframed: GitHub is needed only to work in a GitHub repository, not when `--cloud` bundles a local repo. [[lines 164-169](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/sandbox-environments.md?plain=1#L164-L169)] [[Source](https://code.claude.com/docs/en/sandbox-environments#cloud-sessions)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Mods run outside the sandbox: their file access, network requests, and `$.process` programs aren't sandboxed. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/sandboxing.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/sandboxing#what-runs-outside-the-sandbox)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New `CLAUDE_RUNNER_SPAWN_REASON` variable passed to the `spawn-runner` hook (e.g. `runner_lost`, `resumed`). Requires v2.1.318. [[line 328](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L328)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#the-spawn-runner-hook)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* If a session's provider isn't on the cached `allowedProviders` list, Claude Code can wait for a settings fetch and recheck before refusing. [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/server-managed-settings.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Push notification settings clarified: in a local session they need Remote Control. [[lines 4828](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/settings-reference.md?plain=1#L4828), [4965](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/settings-reference.md?plain=1#L4965)]
* The credential helper reruns after a 401 (not 403) through an LLM gateway when `CLAUDE_CODE_SKIP_VERTEX_AUTH`, `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH` or `CLAUDE_CODE_SKIP_MANTLE_AUTH` is set. Requires v2.1.318. [[line 5175](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/settings-reference.md?plain=1#L5175)] [[Source](https://code.claude.com/docs/en/settings-reference#apikeyhelper)]
* `forceLoginOrgUUID`: outside managed settings Claude Code doesn't check the login's organization. [[line 5261](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/settings-reference.md?plain=1#L5261)] [[Source](https://code.claude.com/docs/en/settings-reference#forceloginorguuid)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Manifest signature verification now uses `gpg --with-fingerprint --verify` and tells you to compare the `Primary key fingerprint` against the one in Step 1. [[lines 535-542](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/setup.md?plain=1#L535-L542)] [[Source](https://code.claude.com/docs/en/setup#verify-the-manifest-signature)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `PushNotification` now also sends a phone push from cloud sessions, and a desktop notification from local sessions. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/tools-reference.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/tools-reference#tools-reference)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* A GitHub account is needed only for GitHub repositories, not when `--cloud` bundles a local repo. [[lines 11](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/web-quickstart.md?plain=1#L11), [43](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/web-quickstart.md?plain=1#L43), [208](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/claude-code/web-quickstart.md?plain=1#L208)]

-----

## API changes

### Changed documents

#### [build-with-claude/compaction-background](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-background.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-background)]

* Background compaction is now listed as beta on Amazon Bedrock. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-background.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-background#set-this-near-your-real-input-budget-it-is-low-here-so-a-short-conversation-compacts)]

#### [build-with-claude/compaction-keep-recent-turns](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-keep-recent-turns.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns)]

* Keep-tail compaction is now listed as beta on Amazon Bedrock. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-keep-recent-turns.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns#set-this-near-your-real-input-budget-it-is-low-here-so-a-short-conversation-compacts)]

#### [build-with-claude/compaction-on-demand](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-on-demand.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand)]

* On-demand compaction is now listed as beta on Amazon Bedrock. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/255938ce92e54bae1a396e1ff699bc5a6c9fc873/docs-md/api/build-with-claude/compaction-on-demand.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand#max_tokens-caps-the-whole-call-including-any-thinking-so-allow-several-thousand-tokens)]
