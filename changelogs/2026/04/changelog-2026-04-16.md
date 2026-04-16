# [Claude docs changes for April 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7530e3a5ef6544db9d27672946fcbf9e4aa70be7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7530e3a5ef6544db9d27672946fcbf9e4aa70be7)]

## Executive Summary
- Version 2.1.110 adds the `/tui` command for flicker-free rendering in the same conversation, mobile push notifications via Remote Control, and fixes MCP tool calls hanging when server connections drop
- Agent SDK gains `excludeDynamicSections` option to move per-session context out of the system prompt, enabling cross-machine prompt cache reuse for fleet deployments
- Code Review's `REVIEW.md` documentation is significantly overhauled — it now acts as the highest-priority system prompt override with detailed guidance on tuning severity, nit volume, skip rules, and repo-specific checks
- Two new environment variables (`CLAUDE_CODE_REMOTE`, `CLAUDE_CODE_REMOTE_SESSION_ID`) make it easy to detect cloud sessions and link generated artifacts back to their source transcript
- claude.ai/code web sessions now support URL query-parameter pre-filling, enabling integrations like issue-tracker buttons that open Claude Code with a pre-loaded prompt and repository

## New Claude Code versions

### [2.1.110](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/versions/2.1.110.md)

#### New features

* Added `/tui` command and `tui` setting — run `/tui fullscreen` to switch to flicker-free rendering in the same conversation
* Added push notification tool — Claude can send mobile push notifications when Remote Control and "Push when Claude decides" config are enabled
* Added `autoScrollEnabled` config to disable conversation auto-scroll in fullscreen mode
* Added option to show Claude's last response as commented context in the `Ctrl+G` external editor (enable via `/config`)
* `--resume`/`--continue` now resurrects unexpired scheduled tasks
* SDK/headless sessions now read `TRACEPARENT`/`TRACESTATE` from the environment for distributed trace linking
* Session recap is now enabled for users with telemetry disabled (Bedrock, Vertex, Foundry, `DISABLE_TELEMETRY`); opt out via `/config` or `CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0`

#### Existing feature improvements

* Changed `Ctrl+O` to toggle between normal and verbose transcript only; focus view is now toggled separately with the new `/focus` command
* Improved `/plugin` Installed tab — items needing attention and favorites appear at the top, disabled items are hidden behind a fold, and `f` favorites the selected item
* Improved `/doctor` to warn when an MCP server is defined in multiple config scopes with different endpoints
* `/context`, `/exit`, and `/reload-plugins` now work from Remote Control (mobile/web) clients
* Write tool now informs the model when you edit the proposed content in the IDE diff before accepting
* Bash tool now enforces the documented maximum timeout instead of accepting arbitrarily large values

#### Major bug fixes

* Fixed MCP tool calls hanging indefinitely when the server connection drops mid-response on SSE/HTTP transports
* Fixed non-streaming fallback retries causing multi-minute hangs when the API is unreachable
* Fixed `PermissionRequest` hooks returning `updatedInput` not being re-checked against `permissions.deny` rules; `setMode:'bypassPermissions'` updates now respect `disableBypassPermissionsMode`
* Hardened "Open in editor" actions against command injection from untrusted filenames
* Fixed stdio MCP servers that print stray non-JSON lines to stdout being disconnected on the first stray line (regression in 2.1.105)
* Fixed `PreToolUse` hook `additionalContext` being dropped when the tool call fails

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/cost-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]

* Added an explicit disclaimer that `total_cost_usd` and `costUSD` are client-side estimates computed from a bundled price table, not authoritative billing data — pricing changes, unrecognized models, and billing rules can cause them to drift from the actual bill. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]
* Updated diagram description and step 2 caption to say "cumulative estimate" rather than "authoritative total". [[lines 29-41](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L29-L41)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#understand-token-usage)]
* Updated troubleshooting guidance to say the result message `total_cost_usd` is the SDK's best estimate, not a billing-authoritative figure. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#resolve-output-token-discrepancies)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Added new section "Improve prompt caching across users and machines" documenting the `excludeDynamicSections` option (`exclude_dynamic_sections` in Python). When set, per-session context (working directory, git status, memory paths) moves from the system prompt into the first user message, allowing a fleet of agents on different machines to share the same cached system prompt. Requires SDK v0.2.98+ (TypeScript) or v0.1.58+ (Python). [[lines 204-240](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L204-L240)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added `exclude_dynamic_sections` optional field to `SystemPromptPreset` with description of its effect on prompt cache reuse. [[lines 829-837](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/python.md?plain=1#L829-L837)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#systempromptpreset)]
* Updated `costUSD` field description to "Estimated cost in USD for this model, computed client-side" with a link to billing caveats. [[line 1420](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/python.md?plain=1#L1420)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Updated `systemPrompt` parameter type to include `excludeDynamicSections?: boolean` and added documentation on its use for cross-machine prompt-cache reuse. [[line 314](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L314)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* Added note to `ModelUsage` that the `costUSD` value is a client-side estimate with a link to billing caveats. [[line 2258](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2258)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#modelusage)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added new "Link artifacts back to the session" section: each cloud session exposes its ID via `CLAUDE_CODE_REMOTE_SESSION_ID`, which can be used to embed a traceable link to the transcript in PR bodies, commit messages, or reports. [[lines 98-104](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L98-L104)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#link-artifacts-back-to-the-session)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Clarified that review results are posted as inline comments with a summary in the review body. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/code-review.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/code-review#how-reviews-work)]
* Significantly overhauled the `REVIEW.md` section: it is now described as highest-priority system prompt override injected into every review agent, taking precedence over default guidance. Added detailed "What you can tune" subsection covering severity redefinition, nit volume caps, skip rules, repo-specific checks, verification bar, re-review convergence, and summary shape. Updated example `REVIEW.md` with a more comprehensive illustration. [[lines 137-198](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/code-review.md?plain=1#L137-L198)] [[Source](https://code.claude.com/docs/en/code-review#customize-reviews)]
* Added new troubleshooting section "Review didn't run and the PR shows a spend-cap message" explaining what happens when monthly spend cap is reached and how to resume. [[lines 236-238](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/code-review.md?plain=1#L236-L238)] [[Source](https://code.claude.com/docs/en/code-review#review-didn’t-run-and-the-pr-shows-a-spend-cap-message)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added disclaimer that the `/cost` command dollar figure is a local estimate and may differ from the actual bill; links to Claude Console for authoritative billing. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/costs.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/costs#using-the-/cost-command)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_REMOTE` env var — set automatically to `true` in cloud sessions, readable from hooks or setup scripts to detect the cloud environment. [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/env-vars.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_REMOTE_SESSION_ID` env var — set automatically in cloud sessions to the current session's ID for constructing transcript links. [[line 115](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/env-vars.md?plain=1#L115)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_TMUX_TRUECOLOR` env var — set to `1` to enable 24-bit truecolor inside tmux (disabled by default since tmux does not pass through truecolor escape sequences unless configured). [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/env-vars.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Clarified that `network.allowUnixSockets` is macOS only — on Linux and WSL2 the seccomp filter cannot inspect socket paths, so `allowAllUnixSockets` must be used instead. [[lines 271-272](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/settings.md?plain=1#L271-L272)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Added new "Pre-fill sessions" section documenting URL query parameters (`prompt`, `prompt_url`, `repositories`, `environment`) that pre-populate a new cloud session — enabling integrations like issue-tracker buttons that open Claude Code with the relevant context already loaded. [[lines 134-152](https://github.com/gpambrozio/ClaudeDocs/blob/7530e3a5ef6544db9d27672946fcbf9e4aa70be7/docs-md/claude-code/web-quickstart.md?plain=1#L134-L152)] [[Source](https://code.claude.com/docs/en/web-quickstart#pre-fill-sessions)]

-----

## API changes

No significant API documentation changes today.
