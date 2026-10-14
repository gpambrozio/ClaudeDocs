# [Claude docs changes for October 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ae4b2a3e1fa330eb5610899a33d96595d819f563) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ae4b2a3e1fa330eb5610899a33d96595d819f563)]

## Executive Summary
- Claude Code 2.1.299 adds idle compaction: a 200K+ token conversation left idle for about 54 minutes is compacted before its one-hour prompt cache expires. It is configurable with `idleCompaction` and `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`.
- New "You should know" built-in mod surfaces one easily missed point per check (a tradeoff Claude made, a result that may be off) as a short note above the prompt.
- New Managed Agents guides on secure deployment: recommended settings, sandbox risks and boundaries, and reviewing and monitoring sessions.
- API docs now use Claude Opus 5.5 (`claude-opus-5-5`) in examples, with updated Opus pricing in the Managed Agents session runtime example ($4 input / $20 output per million tokens).
- Security hardening across 2.1.299: MCP allow rules and agent `tools:` lists now match only the named server, and `UserPromptSubmit` hooks run before skill or slash command expansion.

## New Claude Code versions

### [2.1.299](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/versions/2.1.299.md)

#### New features

* Added `CLAUDE_CODE_DISABLE_FILE_MENTIONS`: Claude gets the paths of `@` file mentions to read with its file tools instead of the files' contents
* Added idle compaction in the terminal: a 200K+ token conversation left idle for about 54 minutes is compacted before its one-hour prompt cache expires. `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` changes the threshold, and `"idleCompaction": false` turns it off
* Added mod APIs for managed-settings mods: `$.prompt.media`, `$.session.identity()`, `size`/`weight`/`mono`/`tabular` on `Text`, named spacing steps on `Box`, skill details passed to the `skill.prompt` hook, and a `queue` door on `session.append`
* Added `--shutdown-drain-sec` to `claude self-hosted-runner orchestrator` for graceful shutdown on SIGTERM
* Added `/effort` and `/fast` in agent view to set what new sessions start with; a bare `/model`, `/effort` or `/fast` there opens a picker
* Added `--disallow-tools` and a `disallowed_tools` case field to `claude plugin eval`
* Added `CLAUDE_CODE_ATTRIBUTION_HEADER=0` support for turning off the attribution block in Claude Desktop's Code tab via a Claude apps gateway policy
* Added `/usage` warnings for max effort, workflows, always-on context and large tool results
* Added a note in `/plugin` and `claude plugin validate` naming a mod's hooks that are skipped where an organization manages Claude Code
* Claude in Slack can now delete a canvas it created

#### Existing feature improvements

* Managed permission rules, managed hooks and organization MCP tool names are enforced better against user-installed mods
* PDFs that are @-mentioned no longer keep their bytes in the session transcript, reducing memory and disk use
* A local session can watch up to 25 published artifacts, up from 10
* Background agent notifications now say when an agent is only waiting on its own background work, got a message too late, or was stopped by a usage limit
* Better errors for worktree creation failures (unresolvable base commit, bare-repository layout) and for the unrecognized model ID startup warning
* Cloud sessions and Remote Control MCP connectors negotiate MCP protocol version 2026-07-28 by default (`MCP_PROTOCOL_NEGOTIATION=legacy` opts out)
* MCP tool descriptions and server instructions from Anthropic's first-party MCP servers are no longer cut at 4,096 characters
* Streams through a custom `ANTHROPIC_BASE_URL` now wait 300 seconds, up from 180, before aborting with no data
* Behavior changes: MCP allow rules and agent `tools:` lists reach only the server they name (`mcp__a` no longer matches `a__b`); `UserPromptSubmit` hooks run before a skill or custom slash command expands; the resume command printed at exit uses the session ID instead of its name; `/ultrareview` errors no longer suggest `git add .`

#### Major bug fixes

* Fixed sandbox escapes: sandboxed commands writing into a `--plugin-dir` folder, reading or writing denied paths through symlinks on macOS, and glob `allowRead`/`allowWrite` entries not being re-checked after a symlink replacement
* Fixed plan mode running writes that a `PreToolUse` hook or a mod's `tool.check` hook allowed
* Fixed third-party gateway API keys being sent to Anthropic for server-managed settings, feature flag and other requests
* Fixed Write dropping byte-order marks or silently converting Windows-1252, Shift-JIS, GBK or UTF-16BE files to UTF-8, and Read garbling UTF-16LE files
* Fixed cloud and headless sessions running an approved tool call twice after a restart (regression in 2.1.296)
* Fixed MCP servers named `constructor` or `prototype` never connecting, and MCP deny/ask rules not applying to servers with a double underscore in their name
* Fixed MCP connections over HTTP hanging for 30 seconds when a server never ends a notification reply
* Fixed images attached while Claude is working being sent at full size, causing repeated image errors in long conversations
* Fixed `/usage`, the limit warning and the status line sometimes showing more than 100% used
* Fixed scheduled tasks and loops misfiring around the daylight saving time change
* Windows: PreToolUse and PermissionRequest hooks that set no shell now block rather than fail open when Git for Windows isn't installed

-----

## Claude Code changes

### Changed documents

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Cloud sessions accept `/model`, `/effort`, `/color` and `/rename` with the value passed as an argument. [[line 253](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L253)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#manage-context)]
* New error messages for organizations that disable cloud sessions or whose policy couldn't be verified. [[lines 395-397](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L395-L397)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#errors-when-sending-to-a-cloud-session)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/cd <path>` moves a session to a new working directory while keeping the conversation. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/commands.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/color`, `/fast`, `/mcp` (reconnect, enable, disable), `/remote-control` and `/rename` entries expanded with new argument and behavior details. [[lines 66-125](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/commands.md?plain=1#L66-L125)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)] and [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/desktop-changelog.md)

* Desktop release notes were updated with new entries (about 200 lines changed in each file).

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_FILE_MENTIONS` to stop `@` mention expansion. [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` (default 200000, minimum 100000). [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` now replaces both default limits: 4096, and 16384 for tools loaded through tool search. [[line 315](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L315)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` raises the backoff ceiling for `529` overloaded retries (32000 to 64000). [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG` shows the last three checks of the You should know mod. [[line 423](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L423)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `DISABLE_AUTO_COMPACT` also disables idle compaction, and `ENABLE_TOOL_SEARCH` default behavior was simplified. [[lines 439-465](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/env-vars.md?plain=1#L439-L465)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New sections for "Failed to fetch session from Sessions API", "Request rejected as unprocessable by the model", and MCP tool names over 128 characters. [[lines 1977-1994](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/errors.md?plain=1#L1977-L1994)] [[Source](https://code.claude.com/docs/en/errors#host-not-allowed-in-a-cloud-session)]
* New sections for cloud-session policy errors ("Cloud sessions use your claude.ai login", "Couldn't verify your organization's policy") and a failed stash when a folder replaces a tracked file. [[lines 2911-2967](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/errors.md?plain=1#L2911-L2967)] [[Source](https://code.claude.com/docs/en/errors#command-line-errors)]
* Retry tuning table lists `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS`. [[line 444](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/errors.md?plain=1#L444)] [[Source](https://code.claude.com/docs/en/errors#tune-retry-behavior)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New section "Hooks that start a background process": print the decision first and redirect the background process's output, or Claude Code blocks the call with `refusing to honor the suspect capture`. [[lines 853-873](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/hooks.md?plain=1#L853-L873)] [[Source](https://code.claude.com/docs/en/hooks#hooks-that-start-a-background-process)]
* The `auto` matcher for `PreCompact` and `PostCompact` now also covers idle compaction. [[lines 3190-3222](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/hooks.md?plain=1#L3190-L3222)] [[Source](https://code.claude.com/docs/en/hooks#precompact)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New "You should know suggestions" section for the built-in mod that shows one note above the prompt when it spots something you might have missed. It covers enabling it (`/plugin enable cc-plugin-you-should-know@builtin`), the cost of background checks, answering notes (Learn more, Knew this already, Dismiss), and turning it off. [[lines 430-483](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/interactive-mode.md?plain=1#L430-L483)] [[Source](https://code.claude.com/docs/en/interactive-mode#you-should-know-suggestions)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* A JSON entry with a `url` but no `type` is a configuration error and the server is skipped. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/mcp#option-1-add-a-remote-http-server)]
* `CLAUDE_PROJECT_DIR` is stable; servers should use MCP `roots/list` for allowed directories. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server)]
* New "How Claude Code stops a stdio server" section describing the signal sequence on macOS/Linux and Windows. [[lines 133-141](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md?plain=1#L133-L141)] [[Source](https://code.claude.com/docs/en/mcp#how-claude-code-stops-a-stdio-server)]
* Reconnect behavior for remote servers in headless and SDK runs, per-server `timeout` as a floor on the idle timeout, and token refresh with one retry on a `401`. [[lines 369-433](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md?plain=1#L369-L433)] [[line 753](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/mcp.md?plain=1#L753)] [[Source](https://code.claude.com/docs/en/mcp#mid-session-drops-of-a-remote-server)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode's default block list was consolidated, removing per-version notes. Handling of pushes to repositories with unknown visibility was clarified. [[lines 380-415](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/permission-modes.md?plain=1#L380-L415)] [[Source](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)]

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* New section on how dependencies resolve when a plugin loads from claude.ai (`<name>@synced`): a dependency counts as met by the marketplace copy or an enabled claude.ai plugin of the same name. [[lines 212-222](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/plugin-dependencies.md?plain=1#L212-L222)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#dependencies-when-your-plugin-loads-from-claudeai)]
* The same addition appears in `plugins/dependencies`.

#### [plugin-evals](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/plugin-evals.md) [[Source](https://code.claude.com/docs/en/plugin-evals)]

* New troubleshooting entry for "cannot be evaluated where sessions load it" and how to evaluate a directory instead. [[lines 665-678](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/plugin-evals.md?plain=1#L665-L678)] [[Source](https://code.claude.com/docs/en/plugin-evals#is-not-a-trusted-plugin-directory-and-this-run-cannot-stop-to-ask-you-about-it)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* The artifact publishing rules moved to a new section, "When a run publishes an artifact without asking". New artifacts can be published without asking, and the conditions for republishing existing ones changed. [[lines 315-332](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/routines.md?plain=1#L315-L332)] [[Source](https://code.claude.com/docs/en/routines#when-a-run-publishes-an-artifact-without-asking)]
* API trigger tokens can now be deleted from the web UI to turn off API access. [[lines 167-171](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/routines.md?plain=1#L167-L171)] [[Source](https://code.claude.com/docs/en/routines#add-an-api-trigger)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `idleCompaction` setting with its conditions, plus how to change the token threshold. [[lines 2913-2955](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/settings-reference.md?plain=1#L2913-L2955)] [[Source](https://code.claude.com/docs/en/settings-reference#idlecompaction)]
* Turning off `autoCompactEnabled` also turns off idle compaction. [[line 2723](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/settings-reference.md?plain=1#L2723)] [[Source](https://code.claude.com/docs/en/settings-reference#autocompactenabled)]
* `CLAUDE_CODE_DISABLE_FILE_MENTIONS` listed among variables ignored in project and local settings. [[line 2884](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/claude-code/settings-reference.md?plain=1#L2884)] [[Source](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)]

-----

## API changes

### New Documents

#### [secure-deployment](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/secure-deployment.md) [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment)]

Guide listing the settings that limit what a Managed Agents agent can reach and do, most important first, with a summary table of recommended values and links to the pages that cover each setting.

#### [secure-deployment-monitoring](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/secure-deployment-monitoring.md) [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment-monitoring)]

Covers optionally running an offline reviewer job that sends each session's events to Claude through the Messages API, watching webhooks for sessions that need attention, and what Managed Agents retains and for how long.

#### [secure-deployment-risks](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/secure-deployment-risks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/secure-deployment-risks)]

Explains why the security settings matter (prompt injection, and Claude using reachable tools or credentials to get past obstacles) and what the Managed Agents sandbox can and cannot do.

### Changed documents

#### [advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* All examples and the quick start now use `claude-opus-5-5` as the advisor model. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#quick-start)]
* The C# example sets a 5 minute client timeout, because advisor calls run a second model inside the request. [[lines 496-497](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L496-L497)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#multi-turn-conversations)]

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* The AWS region is now required, and the SDK errors if none is set. Region comes from `aws_region`, `AWS_REGION`, or `AWS_DEFAULT_REGION`. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#obtain-your-workspace-id)]
* API key authentication (`ANTHROPIC_AWS_API_KEY`) is documented as an option, and the client auth resolution order was rewritten. [[lines 190-259](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L190-L259)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication)]
* `ANTHROPIC_AWS_WORKSPACE_ID` and the `anthropic-workspace-id` header are described. [[line 507](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L507)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#making-requests)]

#### [compliance](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* Two new activity types: `claude_artifact_type_default_updated` and `claude_artifact_type_pin_updated`, bringing the total to 527. The same changes appear in `compliance/activities` and `compliance/activities/list`. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/api/compliance.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/api/compliance#query-parameters)]

#### [dreams](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

* Examples use `claude-opus-5-5`, and the supported models list for the research preview now includes `claude-opus-5-5` and `claude-fable-5-1`. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/dreams.md?plain=1#L159)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams#create-a-dream)]
* The output memory store ID appears in `outputs` shortly after the dream starts running. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/managed-agents/dreams.md?plain=1#L26)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works)]

#### [pricing](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* The Managed Agents session runtime example now uses Claude Opus 5.5 at $4 input / $20 output per million tokens (total $0.58, or $0.428 with prompt caching at a 0.05 cache read multiplier). [[lines 438-455](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/about-claude/pricing.md?plain=1#L438-L455)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#worked-example)]

#### [rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* The rate limit tables are now described per row, with some rows covering several models that share one limit. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/api/rate-limits.md?plain=1#L121)] [[Source](https://platform.claude.com/docs/en/api/rate-limits#cache-aware-itpm)]
* The response headers table notes that not every 429 carries `retry-after`; the spend-cap 429 never does. [[lines 273-293](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/api/rate-limits.md?plain=1#L273-L293)] [[Source](https://platform.claude.com/docs/en/api/rate-limits#response-headers)]

#### [thinking](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* Lists the models where thinking is already on (Opus 5.5, Sonnet 5.5, Fable 5.1, Mythos 5.1, Haiku 5.5, and others) versus those that need `thinking: {type: "adaptive"}` (Opus 4.8, 4.7, 4.6 and Sonnet 4.6). Examples use `claude-opus-5-5`. [[lines 71-73](https://github.com/gpambrozio/ClaudeDocs/blob/ae4b2a3e1fa330eb5610899a33d96595d819f563/docs-md/api/build-with-claude/thinking.md?plain=1#L71-L73)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#configuring-thinking)]
