# [Claude docs changes for April 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e2101e7ea4d21bb085df13a731c83a4f38f67f2b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e2101e7ea4d21bb085df13a731c83a4f38f67f2b)]

## Executive Summary
- HIPAA compliance is now a first-class API feature with full documentation, a signed BAA process, a dedicated HIPAA-enabled org, and a new feature eligibility table showing which API features are HIPAA-eligible
- A new `PermissionDenied` hook event lets hooks respond when auto mode denies a tool call (including the ability to request a retry), and a new `"defer"` decision in `PreToolUse` allows non-interactive callers to pause Claude at a tool call and resume later
- Claude Code 2.1.90 adds `/powerup` interactive feature lessons, fixes critical bugs (rate-limit dialog infinite loop, `--resume` cache miss regression, PostToolUse format-hook edit failures), and delivers multiple quadratic-to-linear performance improvements
- Sub-agents now support managed settings deployment by org admins, an `auto` permission mode, and a `color` display field
- The `settings.json` `showThinkingSummaries` option controls whether extended thinking summaries appear in interactive sessions (default off)

## New Claude Code versions

### [2.1.90](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/versions/2.1.90.md)

#### New features

* Added `/powerup` — interactive lessons that teach Claude Code features with animated demos
* Added `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE` env var to keep the existing marketplace cache when `git pull` fails, useful in offline environments
* Added `.husky` to protected directories in acceptEdits mode

#### Existing feature improvements

* Improved performance: eliminated per-turn JSON.stringify of MCP tool schemas on cache-key lookup
* Improved performance: SSE transport now handles large streamed frames in linear time (previously quadratic)
* Improved performance: SDK sessions with long conversations no longer slow down quadratically on transcript writes
* Improved `/resume` all-projects view to load project sessions in parallel, reducing load times with many projects
* Changed `--resume` picker to no longer show sessions created by `claude -p` or SDK invocations
* Removed `Get-DnsClientCache` and `ipconfig /displaydns` from auto-allow list (DNS cache privacy)
* Hardened PowerShell tool permission checks: fixed trailing `&` background job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, and parse-fail fallback deny-rule degradation

#### Major bug fixes

* Fixed an infinite loop where the rate-limit options dialog would repeatedly auto-open after hitting the usage limit, eventually crashing the session
* Fixed `--resume` causing a full prompt-cache miss on the first request for users with deferred tools, MCP servers, or custom agents (regression since v2.1.69)
* Fixed `Edit`/`Write` failing with "File content has changed" when a PostToolUse format-on-save hook rewrites the file between consecutive edits
* Fixed `PreToolUse` hooks that emit JSON to stdout and exit with code 2 not correctly blocking the tool call
* Fixed auto mode not respecting explicit user boundaries ("don't push", "wait for X before Y") even when the action would otherwise be allowed

-----

## Claude Code changes

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Default primary model for Bedrock changed to `us.anthropic.claude-sonnet-4-5-20250929-v1:0`. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/amazon-bedrock.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]
* New section documenting 1M token context window support for Claude Opus 4.6 and Sonnet 4.6 on Bedrock; Claude Code auto-enables it when a 1M model variant is selected, or append `[1m]` to the model ID for a pinned model. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/amazon-bedrock.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#iam-configuration)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--agent-teams` flag removed; agent teams are now only enabled via the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` env var. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/cli-reference.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New `--include-hook-events` flag that includes all hook lifecycle events in the output stream (requires `--output-format stream-json`). [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/cli-reference.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--maintenance` flag now starts interactive mode after running maintenance hooks instead of just exiting. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/cli-reference.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Note added that `claude --help` does not list every flag. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/cli-reference.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/permissions` command description expanded to cover managing allow/ask/deny rules by scope, adding/removing rules, managing working directories, and reviewing recent auto mode denials. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/commands.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/commands)]
* `/tasks` command now also available as `/bashes`. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/commands.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Extended thinking token billing clarification: thinking tokens are charged even when summaries are redacted; in interactive mode, thinking appears as a collapsed stub by default; `showThinkingSummaries: true` in `settings.json` shows full summaries. [[line 555](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/common-workflows.md?plain=1#L555)] [[Source](https://code.claude.com/docs/en/common-workflows#how-extended-thinking-works)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `MCP_CONNECTION_NONBLOCKING` environment variable: in non-interactive mode (`-p`), setting to `true` skips the MCP connection wait entirely (without it, the first query waits up to 5 seconds for `--mcp-config` server connections). [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/env-vars.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Minimum required version updated to v2.1.89. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/fullscreen.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/fullscreen)]
* Mouse wheel scrolling now documented: requires the terminal to forward mouse events; iTerm2-specific instructions provided (Settings → Profiles → Terminal → Enable mouse reporting). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/fullscreen.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/fullscreen#scroll-the-conversation)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Vertex AI example model IDs updated from `claude-sonnet-4@20250514` to `claude-sonnet-4-5@20250929` and the related env var renamed accordingly. [[line 545](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/github-actions.md?plain=1#L545)] [[Source](https://code.claude.com/docs/en/github-actions#for-aws-bedrock)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Default primary model for Vertex AI changed to `claude-sonnet-4-5@20250929`. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/google-vertex-ai.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#5-pin-model-versions)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New `PermissionDenied` hook event documented: fires when the auto mode classifier denies a tool call; return `{retry: true}` to tell the model it may retry; supports matcher and `if` field. [[line 373](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks-guide.md?plain=1#L373)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]
* New `"defer"` option for `PreToolUse` `permissionDecision`: available in non-interactive (`-p`) mode, pauses the process and lets a calling Agent SDK app resume later. [[line 466](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks-guide.md?plain=1#L466)] [[Source](https://code.claude.com/docs/en/hooks-guide#structured-json-output)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `PermissionDenied` hook event fully documented: fires when auto mode classifier denies a tool call (not on manual denials or `PreToolUse` blocks); matches on tool name; supports `retry: true`; only supports `command` and `http` hook types. [[lines 1161-1210](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks.md?plain=1#L1161-L1210)] [[Source](https://code.claude.com/docs/en/hooks#posttoolusefailure-decision-control)]
* New `"defer"` decision value for `PreToolUse` `permissionDecision`: allows non-interactive callers to pause Claude at a tool call, collect input externally, then resume; includes the `deferred_tool_use` payload in the SDK result, `stop_reason: "tool_deferred"`, and `stop_reason: "tool_deferred_unavailable"`; requires v2.1.89+. [[lines 912-978](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks.md?plain=1#L912-L978)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-input)]
* Hook output size cap documented: output injected into context is capped at 10,000 characters; excess is saved to a file and replaced with a preview. [[line 543](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/hooks.md?plain=1#L543)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]

#### [Index](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Windows CMD installation troubleshooting note added for users seeing "The token '&&' is not a valid statement separator", directing them to use the PowerShell command instead. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/index.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/index#get-started)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Pasting text that starts with `!` into an empty prompt now automatically enters bash mode, matching the typed `!` behavior. [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/interactive-mode.md?plain=1#L230)] [[Source](https://code.claude.com/docs/en/interactive-mode#bash-mode-with-prefix)]

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New `best` model alias added that always resolves to the most capable available model (currently equivalent to `opus`). [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/model-config.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* `default` alias clarified: it clears any model override rather than itself being a model alias. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/model-config.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]

#### [Network Config](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Download URL documentation corrected: `storage.googleapis.com` is now described as the download bucket for the Claude Code binary and auto-updater; `downloads.claude.ai` is the CDN for install scripts, version pointers, manifests, signing keys, and plugin executables. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/network-config.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [Output Styles](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Token usage impact documented: output styles increase input tokens (offset by prompt caching); built-in Explanatory/Learning styles increase output tokens by design; custom style token usage depends on the instructions given. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/output-styles.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/output-styles#how-output-styles-work)]

#### [Permission Modes](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode denials are now surfaced in `/permissions` under a "Recently denied" tab; approving resets the denial counters. [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/permission-modes.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Setting names corrected to use full dotted paths: `permissions.disableBypassPermissionsMode` and `permissions.disableAutoMode`. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/permissions.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* New "Review auto mode denials" section: auto mode denials are recorded in `/permissions` under a "Recently denied" tab; press `r` on a denied action to mark it for retry and resume the conversation. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/permissions.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Relative path resolution behavior documented: when using a local `directory` or `file` source with a relative path, it resolves against the repository's main checkout (not a worktree); marketplace state stored per-user in `~/.claude/plugins/known_marketplaces.json`. [[line 551](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/plugin-marketplaces.md?plain=1#L551)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#require-marketplaces-for-your-team)]

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `PermissionDenied` hook event added to the supported hook events table. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/plugins-reference.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Windows CMD installation troubleshooting note added for users seeing "The token '&&' is not a valid statement separator". [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/overview.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/overview#get-started)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Windows CMD installation troubleshooting note added for users seeing "The token '&&' is not a valid statement separator". [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/quickstart.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]

#### [Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Recurring task automatic expiry extended from 3 days to 7 days. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/scheduled-tasks.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#jitter)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `cleanupPeriodDays` behavior changed: setting to `0` is now rejected with a validation error (minimum is now 1); transcript disabling in non-interactive mode now uses `--no-session-persistence` or `persistSession: false`. [[line 156](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/settings.md?plain=1#L156)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `forceLoginOrgUUID` now accepts an array of UUIDs (any listed org is accepted); an empty array blocks all logins. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/settings.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `showThinkingSummaries` setting: controls whether extended thinking summaries appear in interactive sessions; default is `false` (collapsed stub); non-interactive mode and SDK callers always receive summaries. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/settings.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Binary verification documentation significantly expanded: step-by-step guide for verifying manifest signatures with GPG (Anthropic signing key fingerprint `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`; available for v2.1.89+); per-platform binary checksum verification; macOS (`codesign`) and Windows (`Get-AuthenticodeSignature`) code signature verification commands. [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/setup.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/setup#install-with-npm)]
* Windows CMD installation troubleshooting note added for users seeing "The token '&&' is not a valid statement separator". [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/setup.md?plain=1#L49)] [[Source](https://code.claude.com/docs/en/setup#install-claude-code)]

#### [Sub-Agents](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Managed subagents added as highest-priority scope (priority 1): organization admins can deploy subagents via `.claude/agents/` in the managed settings directory. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* `auto` added to `permissionMode` options: AI classifier evaluates each tool call. [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md?plain=1#L217)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* New `color` frontmatter field: subagents can be assigned a display color in the task list and transcript; accepts `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, or `cyan`. [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md?plain=1#L226)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Running background subagents now appear in @-mention typeahead with their status shown. [[line 564](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md?plain=1#L564)] [[Source](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)]
* `--agent-teams` flag removed; activation is now only via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. [[line 657](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/sub-agents.md?plain=1#L657)] [[Source](https://code.claude.com/docs/en/sub-agents#resume-subagents)]

#### [Tools Reference](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `SendMessage`, `TeamCreate`, `TeamDelete` tool descriptions updated to remove `--agent-teams` flag references; activation is now only via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/claude-code/tools-reference.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/tools-reference)]

-----

## API changes

### Changed documents

#### [API and Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

* HIPAA compliance introduced as a first-class arrangement alongside ZDR: getting started requires signing a BAA and being provisioned a dedicated HIPAA-enabled organization; HIPAA-enabled orgs automatically block non-eligible features with a `400` error. [[lines 4-8](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L4-L8)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]
* PHI handling guidelines documented: PHI must not appear in JSON schema definitions (property names, `enum`/`const`/`pattern`), as compiled schemas are cached separately and do not receive the same PHI protections as prompts/responses. [[lines 90-108](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L90-L108)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]
* Feature eligibility table expanded with a "HIPAA eligible" column for every feature. Notable HIPAA-ineligible features: web fetch, context management/compaction, context editing, computer use, tool search, batch processing, code execution, Files API, agent skills, MCP connector. Structured outputs are HIPAA-eligible with the PHI-in-schema restriction. [[lines 133-168](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L133-L168)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]
* HIPAA error handling documented: describes the `400` error response returned when a HIPAA-enabled org uses a non-eligible feature, with the error payload format. [[lines 110-125](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L110-L125)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]
* New FAQ entries covering HIPAA vs. ZDR differences, whether ZDR is needed alongside HIPAA, behavior when using non-eligible features, using the same org for mixed workloads, and how to request HIPAA API access. [[lines 181-200](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L181-L200)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New Intuit Mailchimp MCP server added: allows creating marketing campaigns via `https://ai-inc.mailchimp.com/claude/mcp/v2`. [[line 726](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L726)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Strict Tool Use](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

* New "Data retention" section: strict tool use is HIPAA eligible, but PHI must not be included in tool schema definitions (property names, `enum`/`const` values, `pattern` regex); compiled schemas are cached separately and do not receive the same PHI protections. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md?plain=1#L102)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Structured outputs now stated to be HIPAA eligible, with the restriction that PHI must not be included in JSON schema definitions (property names, `enum`/`const`/`pattern`). [[line 406](https://github.com/gpambrozio/ClaudeDocs/blob/e2101e7ea4d21bb085df13a731c83a4f38f67f2b/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L406)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
