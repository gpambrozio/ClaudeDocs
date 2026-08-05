# [Claude docs changes for August 5th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/939646871028932d679c68f5596106622c897ea7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/939646871028932d679c68f5596106622c897ea7)]

## Executive Summary
- New native PowerShell tool and hook support brings Windows shell handling to parity with Bash: hooks, permission checks, and tool-search coverage now recognize `Bash|PowerShell` uniformly.
- Sandbox credential masking (`mode: "mask"`) is now documented for `sandbox.credentials.files` on Linux/WSL, letting sandboxed commands use real secrets through a proxy without the container ever seeing the plaintext value.
- Ultraplan has been removed: the `/ultraplan` command, its keyword trigger, and the plan-approval option are gone, with Plan mode taking its place across the docs.
- The auto-compact window is now configurable via `/autocompact`, `--autocompact`, or `CLAUDE_CODE_AUTO_COMPACT_WINDOW`, giving explicit control over when a session starts compacting.
- Claude Code 2.1.222 closes two security-relevant bugs: worktree-isolated sessions could run destructive git commands against the main checkout, and `PreToolUse` auto-allow hooks could bypass tool restrictions inside background agent tasks.

## New Claude Code versions

### [2.1.222](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/versions/2.1.222.md)

#### Existing feature improvements

* Improved auto mode safety: messages sent to other agent sessions via `SendMessage` are now evaluated by the permission classifier before dispatch
* Improved the refusal when Claude tries to invoke a skill with `disable-model-invocation`: Claude is now told to ask you to run the skill instead of replicating its workflow
* Improved the `/diff` view, the Remote Control workspace diff, and file-edit diffs in Claude Code on the web sessions to use raw git blob content, ignoring workspace-configured diff drivers and textconv
* Changed Remote Control auto-start so repo-local settings (`.claude/settings.json` or `.claude/settings.local.json`) can no longer turn it on (they can still turn it off); enable it at user scope via `/config`
* Removed the Ultraplan feature

#### Major bug fixes

* Fixed worktree-isolated sessions and their subagents being able to run destructive git commands against the main checkout; isolation now applies to file edits and Bash in every session type
* Fixed `PreToolUse` auto-allow hooks bypassing tool restrictions in background agent tasks (summaries, compaction, renames)
* Fixed `/usage-credits` on Team and Enterprise showing "you've already sent a usage credit request" for members whose earlier request was dismissed, blocking them from sending a new one
* Fixed the startup connectivity check hanging and then failing behind an HTTPS proxy; it now uses the same proxy-aware transport as API requests and times out with a clear message
* Fixed "Connection closed mid-response" errors being reported on responses that had actually completed
* Fixed `/usage` overattributing usage to MCP servers: a server's share now reflects only the requests that actually consumed its tool results, instead of every turn after any call to it
* Fixed sessions not linking to pull requests created after the branch was pushed, including through the GitHub REST API
* Fixed org-restricted `model: opus`-style subagent and teammate family aliases dropping to the parent model instead of stepping down to the newest org-allowed model in the family
* Fixed stream idle timeout firing on custom `ANTHROPIC_BASE_URL` gateways despite server keep-alive pings arriving on the wire
* Fixed claude.ai connectors being falsely marked as needing authorization when the session token is invalid — they now show a `/login` hint instead
* Fixed tool errors not being displayed for tools no longer available locally, for example after an MCP server is removed
* Fixed screen readers re-reading the whole input line on every backspace in `--ax-screen-reader` mode — end-of-line deletions now echo just the deleted characters

-----

## Claude Code changes

### New Documents

#### [agent-sdk/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/troubleshooting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/troubleshooting)]

New Agent SDK troubleshooting reference, keyed to the error you see. Covers `CLINotFoundError: Claude Code not found` (the Python SDK can't find a `claude` executable), `CLIConnectionError: Refusing to execute batch script` (the SDK refuses to spawn `claude.cmd`/other batch scripts on Windows because `cmd.exe` re-parsing makes them injectable, with guidance to install a native `claude.exe` instead), and `structured_output` coming back `None`/`undefined` on an otherwise-successful run (e.g. from an unsatisfiable schema). Also links to the SDK repos for filing new issues.

### Changed documents

#### [accessibility](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/accessibility.md) [[Source](https://code.claude.com/docs/en/accessibility)]

* Screen-reader-friendly character-level echo in `--ax-screen-reader` mode now also covers `Backspace` deletions at the end of the input line, not just typing. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/accessibility.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/accessibility#what-your-screen-reader-hears)]

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Clarifies that the TypeScript and Python Agent SDKs bundle a native Claude Code binary for most installs (previously stated unconditionally), pointing to the quickstart for exceptions. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]
* The tool-definition context-cost table now describes MCP tool-search fallback to upfront loading as affecting "unsupported models and certain platforms" rather than enumerating each platform individually. [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#what-consumes-context)]

#### [agent-sdk/hosting](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/hosting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]

* Runtime dependency note updated: the bundled Claude Code binary covers most installs, not all; links to the quickstart for which installs need a separately installed native binary. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/hosting.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/agent-sdk/hosting#runtime-dependencies)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* New "Connection timing" table defines exactly which server types delay the first turn and their wait timeouts (stdio/uncached HTTP-SSE block on `MCP_TIMEOUT`, cached remote servers don't block, in-process SDK servers never block), plus two ways to make startup itself block on connection: `MCP_CONNECTION_NONBLOCKING=0` (capped by `MCP_CONNECT_TIMEOUT_MS`) or `alwaysLoad: true` per server. [[lines 140-153](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L140-L153)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)]
* Clarifies exactly when the `init` message is emitted relative to the first-turn wait, and what status/tools each server type shows at that point. [[line 206](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L206)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#discover-available-tools)]
* `"pending"` status is now documented as covering two distinct cases: a settings-file server that didn't get the full startup wait, or a cached-tool-list server not yet actually connected. [[lines 725-726](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L725-L726)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#error-handling)]

#### [agent-sdk/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* New documented edge cases where the SDK does *not* bundle a native Claude Code binary — pip installing the Python SDK's source distribution (e.g. ARM64 Windows) and npm installs that skip optional dependencies (e.g. `npm ci --omit=optional`) — each with a workaround. [[lines 82-85](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L82-L85)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#setup)]

#### [agent-sdk/skills](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/skills.md) [[Source](https://code.claude.com/docs/en/agent-sdk/skills)]

* In the TypeScript SDK, the `skills` option now requires exact Skill names: `query()` throws before starting Claude Code for empty names, names with parentheses/commas/control characters, padded whitespace, or wildcard forms (a bare `*` or a `:*` suffix). Use `skills: "all"` instead of a wildcard. [[lines 85-92](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/skills.md?plain=1#L85-L92)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills#using-skills-with-the-sdk)]

#### [agent-sdk/tool-search](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/tool-search.md) [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search)]

* Tool search is now on by default on Google Cloud's Agent Platform for Claude Opus/Sonnet/Haiku 4.5+ (v2.1.221, same minimums as elsewhere); earlier Agent Platform models still get upfront loading with no `ENABLE_TOOL_SEARCH` override. Previously tool search was off by default for the whole platform. [[lines 17-26](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/tool-search.md?plain=1#L17-L26)] [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search#how-tool-search-works)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* The `skills` option table now documents that the SDK rejects malformed or wildcard skill names with an error before starting the process. [[line 439](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L439)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* Same "bundled for most installs" caveat added for the native Claude Code binary. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#installation)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `/fork`'s copy now makes code changes in its own new worktree rather than potentially sharing the original session's checkout (except bare-repo layouts or worktree isolation off); when the copy starts in the main working tree, it bases a new branch on the original session's branch. [[lines 312-316](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-view.md?plain=1#L312-L316)] [[Source](https://code.claude.com/docs/en/agent-view#copy-the-session-with-/fork)]
* Background-session git workflow reorganized into explicit rules: commit-and-push, open a draft PR when warranted, never push to main/force-push/merge, and defer to your own git-handling instructions in the task, `CLAUDE.md`, or memory. [[lines 412-417](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-view.md?plain=1#L412-L417)] [[Source](https://code.claude.com/docs/en/agent-view#how-file-edits-are-isolated)]
* `/status` now shows a `Session kind` row — background job (`attached`/`unattended`) vs. `interactive` — as of v2.1.221. [[line 520](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/agent-view.md?plain=1#L520)] [[Source](https://code.claude.com/docs/en/agent-view#how-background-sessions-are-hosted)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Plugin install troubleshooting (Telegram, Discord, iMessage, fakechat) now documents that Claude Code auto-refreshes a stale marketplace catalog and retries before reporting "not found," and that the install summary — not a blanket instruction — determines whether `/reload-plugins` is needed. [[lines 34-39](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/channels.md?plain=1#L34-L39)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Claude Code now forwards parent-supplied `sandbox.credentials` in stripped form: `deny` entries keep only path/name and mode, `mode: mask` file entries are forwarded sentinel-only (with empty `injectHosts`, dropping `extract`/`onExtractNoMatch`/`maskDuplicates`), and `mode: mask` `envVars` entries aren't forwarded at all. [[lines 281-285](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-apps-gateway.md?plain=1#L281-L285)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#restrict-parent-settings)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New gateway validation: a non-string `model` value in a request is now rejected with `400 model must be a string`, requiring gateway v2.1.221+. [[line 395](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L395)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` is now described as moving compaction earlier within the auto-compact window, with the new `/autocompact` command and `CLAUDE_CODE_AUTO_COMPACT_WINDOW` for changing the window itself. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#manage-context)]
* Claude Code now computes web diffs (including per-file diffs shown as Claude edits) from raw git blob content, so repository `diff`/`textconv` filters don't apply. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#review-changes)]
* Ultraplan references removed from this page following the feature's removal. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#tips-for-cloud-tasks)]

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* Same marketplace auto-refresh-and-retry plus install-summary-driven `/reload-plugins` guidance added as in channels.md. [[lines 26-29](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/claude-security.md?plain=1#L26-L29)] [[Source](https://code.claude.com/docs/en/claude-security#install-the-plugin)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--autocompact <auto|tokens>` flag sets the auto-compact window for a single session launch, requires v2.1.221+. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/cli-reference.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Clarifies exactly which run types always get text-based findings (terminal `/code-review` forked-subagent runs, and `-p` text/JSON runs) versus host apps (e.g. the desktop app) that get the structured `ReportFindings` list. [[lines 286-291](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/code-review.md?plain=1#L286-L291)] [[Source](https://code.claude.com/docs/en/code-review#review-a-diff-locally)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/autocompact [auto|<tokens>]` command sets the auto-compact window and saves it to user settings, v2.1.221+. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/commands.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/ultraplan` is marked removed; use plan mode instead. [[line 127](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/commands.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* New "Set the auto-compact window" section documents three configuration layers (`/autocompact` command, `--autocompact` flag, `CLAUDE_CODE_AUTO_COMPACT_WINDOW` env var) with precedence rules, accepted value forms (100K-1M tokens), and which sessions compact earlier by default (cloud sessions, Sonnet/Opus 4.6 without extended context, Sonnet 5). [[lines 93-118](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/context-window.md?plain=1#L93-L118)] [[Source](https://code.claude.com/docs/en/context-window#when-your-context-fills-up)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Clarifies that the context/auto-compact warning refers to the session's (now configurable) auto-compact window rather than the model's raw maximum input size. [[line 640](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/costs.md?plain=1#L640)] [[Source](https://code.claude.com/docs/en/costs#understanding-changes-in-claude-code-behavior)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Renaming a session in the desktop app now syncs to the underlying CLI session name, visible via `claude agents` in a terminal; requires v2.1.221+. [[line 293](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/desktop.md?plain=1#L293)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Plugin install failure handling now auto-refreshes a stale marketplace catalog and retries before reporting "not found" when auto-update is on; before v2.1.221 this required a manual `/plugin marketplace update`. [[lines 35-38](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/discover-plugins.md?plain=1#L35-L38)] [[Source](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)]
* The install summary now reports one of `Plugin is now active.`, `Run /reload-plugins to activate.`, or a load failure shown in the `/plugin` Errors tab, instead of every install always requiring a manual reload/restart. [[lines 279-285](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/discover-plugins.md?plain=1#L279-L285)] [[Source](https://code.claude.com/docs/en/discover-plugins#install-plugins)]
* `/reload-plugins` now warns and skips instead of applying when the reload would invalidate the prompt cache, requiring `--force` to proceed. [[line 358](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/discover-plugins.md?plain=1#L358)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `BASH_MAX_OUTPUT_LENGTH` now documents concrete default (30000) and maximum (150000) values. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `BASH_MAX_TIMEOUT_MS`: the effective ceiling is now documented as the larger of this and `BASH_DEFAULT_TIMEOUT_MS`. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md?plain=1#L159)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_AUTO_COMPACT_WINDOW` var documents its accepted range (100000-1000000), that it only accepts a plain integer, and its precedence over `/autocompact`/`--autocompact`/the `autoCompactWindow` setting. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_RESUME_INTERRUPTED_TURN`: fixed so setting the value to `0` disables resume (previously only unsetting it worked). [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md?plain=1#L292)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `ENABLE_TOOL_SEARCH` updated to reflect the new default-on tool search for Claude 4.5+ models on Google Cloud's Agent Platform. [[line 371](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/env-vars.md?plain=1#L371)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* When a server error, dropped connection, or stalled stream hits mid-response after Claude has already completed a text block or tool call, Claude Code now still runs any tool calls Claude already completed and continues the turn from their results, instead of just ending the turn; same updated behavior for "Socket is closed." [[line 118](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/errors.md?plain=1#L118)] [[Source](https://code.claude.com/docs/en/errors#automatic-retries)]
* New documented error "Your checkout has no branches": `/code-review ultra` and `claude ultrareview` now refuse to review a detached-HEAD checkout with no branches before starting a cloud session, requires v2.1.221+. [[lines 1234-1245](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/errors.md?plain=1#L1234-L1245)] [[Source](https://code.claude.com/docs/en/errors#your-checkout-has-no-branches)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Switching to Opus 4.7 now turns fast mode off like any other unsupported model, instead of leaving it on and having the API reject requests (fixed in v2.1.221). [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/fast-mode.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/fast-mode#switch-models-while-fast-mode-is-on)]
* New fallback when usage credits run out mid-session: Claude Code retries each rejected fast-mode request at standard speed/pricing (no cooldown), with a notification in interactive sessions and a `system`/`notification` message in `stream-json`/SDK sessions. [[lines 142-145](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/fast-mode.md?plain=1#L142-L145)] [[Source](https://code.claude.com/docs/en/fast-mode#handle-rate-limits)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Tool search availability on Google Cloud's Agent Platform changed from "off by default platform-wide" to "unsupported only on models earlier than the Claude 4.5 generation." [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/feature-availability.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)]
* Ultraplan removed from the list of claude.ai-only features. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/feature-availability.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/feature-availability#features-that-require-a-claude-subscription)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Tool search on Vertex AI is now on by default for Claude Opus/Sonnet/Haiku 4.5+ (previously required `ENABLE_TOOL_SEARCH=true`); earlier models still load upfront regardless. New `ENABLE_TOOL_SEARCH=false` opt-out documented, effective v2.1.221. [[lines 123-128](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/google-vertex-ai.md?plain=1#L123-L128)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Hooks now run consistently everywhere Claude Code runs — sessions in the terminal, IDE extensions, the desktop app, and Claude Code on the web all fire the same hook events. [[line 5](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L5)] [[Source](https://code.claude.com/docs/en/hooks)]
* New native PowerShell hook support: match `Bash|PowerShell` to cover shell-command hooks on Windows, with a documented PowerShell tool field table and an example `.ps1` hook script. [[lines 103-165](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L103-L165)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* Hook deduplication changed: a handler defined in more than one settings file now runs once, but a plugin's or skill's copy of the same handler stays separate — previously dedup was purely by command string/args or URL. [[line 370](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L370)] [[Source](https://code.claude.com/docs/en/hooks#hook-handler-fields)]
* Cloud sessions on Claude Code on the web don't read your local `~/.claude/settings.json`; hooks there come from the repo and your organization's server-managed settings. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]
* `PostToolUseFailure`'s `error` field format is now documented in detail: a first line `Exit code N` for Bash/PowerShell, `[Request interrupted by user for tool use]` for cancellations, a bare failure message when the shell process itself couldn't start, and middle-truncation past 10,000 characters. [[lines 1757-1770](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L1757-L1770)] [[Source](https://code.claude.com/docs/en/hooks#posttoolusefailure-input)]
* Async hooks: in non-interactive mode (`-p`), Claude Code now kills any async hook still running at teardown and finalizes it with outcome `cancelled`; work that must outlive the session should start a fully detached process. [[lines 2971-2974](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks.md?plain=1#L2971-L2974)] [[Source](https://code.claude.com/docs/en/hooks#configure-an-async-hook)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Hooks needing full shell-command coverage must now match `Bash|PowerShell`, not just `Bash`, since Claude can also run shell commands via the PowerShell tool. [[line 625](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks-guide.md?plain=1#L625)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]
* Shell-form command hooks on Windows now fall back to PowerShell when Git Bash isn't installed (previously always used Git Bash). [[line 937](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/hooks-guide.md?plain=1#L937)] [[Source](https://code.claude.com/docs/en/hooks-guide#json-validation-failed)]

#### [large-codebases](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/large-codebases.md) [[Source](https://code.claude.com/docs/en/large-codebases)]

* Plugin-install failure handling now auto-refreshes a stale marketplace catalog and retries before reporting "plugin not found"; manual `/plugin marketplace update` is only needed if auto-update is disabled. [[lines 188-191](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/large-codebases.md?plain=1#L188-L191)] [[Source](https://code.claude.com/docs/en/large-codebases#reduce-file-reads-with-code-intelligence)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* `serverCommand`/`serverUrl` policy entries in `allowedMcpServers`/`deniedMcpServers` now expand `${VAR}` from a pinned environment rather than the live process environment, closing a bypass where a project/user settings-defined variable could redefine what an allowlist entry matches; `deniedMcpServers` still widens from settings-file variables. Effective v2.1.219. [[lines 167-176](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/managed-mcp.md?plain=1#L167-L176)] [[Source](https://code.claude.com/docs/en/managed-mcp#how-policy-entries-expand)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Same Vertex AI tool-search default change as google-vertex-ai.md — on by default for Claude 4.5+ generation models on Google Cloud's Agent Platform as of v2.1.221; `ENABLE_TOOL_SEARCH` behavior table updated accordingly. [[lines 1078-1092](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/mcp.md?plain=1#L1078-L1092)] [[Source](https://code.claude.com/docs/en/mcp#configure-tool-search)]
* Plugin install failures now auto-retry after refreshing a stale marketplace catalog; the install summary, not a blanket instruction, tells you whether `/reload-plugins` is needed. [[lines 37-42](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/mcp.md?plain=1#L37-L42)] [[Source](https://code.claude.com/docs/en/mcp#find-and-build-mcp-servers)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `acceptEdits` PowerShell auto-approval now excludes commands with a quoted positional argument containing a quote character (e.g. an apostrophe) — these still prompt; use a named parameter like `-Value` to avoid it. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/permission-modes.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)]
* Switching permission modes while an auto-mode classifier check is pending now discards the pending verdict — you're re-prompted (or auto-denied in `dontAsk` mode) instead of a stale verdict being applied. [[line 274](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/permission-modes.md?plain=1#L274)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]
* The "No, refine with Ultraplan" option was removed from the plan-approval dialog. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/permission-modes.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/permission-modes#review-and-approve-a-plan)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Plugin install no longer always requires a manual `/reload-plugins` afterward — it can activate automatically, and the install summary now tells you whether to run it. [[lines 102-107](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/plugin-marketplaces.md?plain=1#L102-L107)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#walkthrough-create-a-local-marketplace)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Same reload-plugins/install-summary change — check the install summary for `Run /reload-plugins to activate.` instead of always running it. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/plugins.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/plugins#add-skills-to-your-plugin)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Falling back to standard speed after running out of fast-mode usage credits mid-session now also preserves the prompt cache, matching the existing rate-limit fallback behavior. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/prompt-caching.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/prompt-caching#turning-on-fast-mode)]
* Installing a plugin from the `/plugin` interface can now activate it immediately without `/reload-plugins`; cache-cost timing follows whenever the change actually applies. [[lines 84-85](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/prompt-caching.md?plain=1#L84-L85)] [[Source](https://code.claude.com/docs/en/prompt-caching#enabling-or-disabling-a-plugin)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Renaming a session from claude.ai or the Claude app now also updates the session's name in the local CLI (prompt bar and `claude agents`), not just the `claude --resume` title. Requires v2.1.221+. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/remote-control.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/remote-control#connect-from-another-device)]
* New remote-only support for `/autocompact`: pass a window size (e.g. `/autocompact 500k`) or run with no argument to print the current window size. [[line 245](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/remote-control.md?plain=1#L245)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]

#### [sandbox-environments](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandbox-environments.md) [[Source](https://code.claude.com/docs/en/sandbox-environments)]

* `--dangerously-skip-permissions` now refuses to start when run as root on Linux/macOS. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandbox-environments.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/sandbox-environments#how-isolation-relates-to-permission-modes)]
* Substantially expanded setup guidance for `@anthropic-ai/sandbox-runtime`: required Linux/WSL2 packages (`bubblewrap`, `socat`, `ripgrep`), required write grants (project dir, `~/.claude`, `~/.claude.json`, `/tmp`), required network domains (provider endpoint plus `claude.ai`/`platform.claude.com` for OAuth), and a note that Linux/WSL2 only grants writes to paths that already exist. [[lines 61-84](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandbox-environments.md?plain=1#L61-L84)] [[Source](https://code.claude.com/docs/en/sandbox-environments#sandbox-runtime)]
* New documentation of built-in deny protections (`.git/hooks`, `.git/config`, `.mcp.json`, `.claude/commands`, `.claude/agents`, shell startup files) and platform differences (macOS checks per-write; Linux/WSL2 builds the deny list once at launch), plus guidance to review writable paths after unattended runs. [[lines 94-109](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandbox-environments.md?plain=1#L94-L109)] [[Source](https://code.claude.com/docs/en/sandbox-environments#what-the-runtime-blocks-on-its-own)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New table details whether a managed `credentials.files` entry pins `filesystem.disabled` — only `mode: "deny"` (or a `mask` entry degraded to `deny` by validation) pins it. [[lines 188-205](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandboxing.md?plain=1#L188-L205)] [[Source](https://code.claude.com/docs/en/sandboxing#which-settings-can-disable-it)]
* Clarifies which protections keep applying with filesystem isolation off (env-var `deny`/`mask` and file `mask` entries still enforced; only file `deny`/`denyRead` and TMPDIR redirection are lifted); notes `$TMPDIR` can now expand empty on Linux, so Claude is told to use `mktemp -d`. [[lines 207-220](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandboxing.md?plain=1#L207-L220)] [[Source](https://code.claude.com/docs/en/sandboxing#what-changes-when-filesystem-isolation-is-off)]
* Major new feature: `credentials.files` entries now support `"mode": "mask"` (previously `deny`-only), requiring `network.tlsTerminate` and v2.1.221+. On Linux/WSL2, sandboxed commands see a sentinel copy of the file with the proxy substituting the real value on egress to `injectHosts`; on macOS the file is simply unreadable (same as `deny`). New `extract`, `onExtractNoMatch`, and `maskDuplicates` fields documented, plus fallback-to-`deny` conditions (directories, globs, files >8MiB, non-UTF-8). [[lines 250-325](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandboxing.md?plain=1#L250-L325)] [[Source](https://code.claude.com/docs/en/sandboxing#mask-credentials)]
* The protected settings-file deny list now also includes `.mcp.json` at the project root and at each `--add-dir`/`/add-dir` root, not just `settings.json` files. [[lines 488-491](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sandboxing.md?plain=1#L488-L491)] [[Source](https://code.claude.com/docs/en/sandboxing#security-limitations)]

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Same plugin-install auto-retry/install-summary changes as the other plugin docs. [[lines 377-384](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/security-guidance.md?plain=1#L377-L384)] [[Source](https://code.claude.com/docs/en/security-guidance#related-resources)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Renaming a session from claude.ai/the Claude app, or from the desktop app, now applies the same name in the CLI. Requires v2.1.221+. [[lines 72-73](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/sessions.md?plain=1#L72-L73)] [[Source](https://code.claude.com/docs/en/sessions#name-your-sessions)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Invalid `sandbox.credentials` `files`/`envVars` entries that still have a valid path/name and a `mask`/`deny` mode are now degraded to `mode: "deny"` with a warning rather than stripped outright, so the credential stays blocked (v2.1.221; previously every invalid entry was stripped). [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/settings.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)]
* New `autoCompactWindow` setting configures the context-window fill threshold (100,000-1,000,000 tokens) for auto-compaction. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/settings.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `disableAutoMode` can now also be set under `permissions.disableAutoMode`. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/settings.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `credentials.files` now supports `mode: "mask"`, plus new `extract`, `onExtractNoMatch`, `maskDuplicates`, and `injectHosts` fields. [[lines 393-397](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/settings.md?plain=1#L393-L397)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* In non-interactive sessions, Claude Code no longer reserves the `help`/`feedback` command names for terminal-only built-ins, so a plugin skill using those names keeps its bare command (a regression from v2.1.216, fixed in v2.1.221). [[line 252](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/skills.md?plain=1#L252)] [[Source](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* The `ultraplan` keyword was removed from the rainbow-gradient-highlighted keywords in the prompt input — only `ultrathink` remains. [[line 118](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/terminal-config.md?plain=1#L118)] [[Source](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* In auto mode (and plan mode while the classifier reviews commands), the auto-mode classifier now reviews each `SendMessage` send before delivery, requires v2.1.222+. [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/tools-reference.md?plain=1#L132)] [[Source](https://code.claude.com/docs/en/tools-reference#timeout-and-output-limits)]
* Reworked "Output limits": Bash output streams to a working file as the command runs (killed past 5GB); how much reaches Claude inline now depends on whether the result counts as valid vs. failure — valid results get ~30,000 chars inline then a file path, failures get a ~10,000-char head/tail excerpt with no file. New table lists which commands' exit code 1 counts as benign (`grep`, `rg`, `find`, `diff`, `test`, `git diff`, `git grep`, etc.) vs. failure. [[lines 140-158](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/tools-reference.md?plain=1#L140-L158)] [[Source](https://code.claude.com/docs/en/tools-reference#output-limits)]
* PowerShell tool commands are now visible to `PreToolUse` hooks via `tool_input.command`; hooks inspecting shell commands should match `Bash|PowerShell`. [[lines 292-293](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/tools-reference.md?plain=1#L292-L293)] [[Source](https://code.claude.com/docs/en/tools-reference#powershell-tool)]

#### [ultraplan](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/ultraplan.md) [[Source](https://code.claude.com/docs/en/ultraplan)]

* The Ultraplan research-preview feature has been removed entirely — the `/ultraplan` command, the `ultraplan` keyword trigger, and the "No, refine with Ultraplan" plan-approval option are all gone. The page now just redirects to Plan mode and Claude Code on the web. [[lines 1-15](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/ultraplan.md?plain=1#L1-L15)] [[Source](https://code.claude.com/docs/en/ultraplan)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* The "No merge base" fallback is clarified and cross-referenced to the new "no branches" refusal case added in errors.md; the "Plan complex changes with ultraplan" related-resource link was removed. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/ultrareview.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/ultrareview#diff-limits-and-fallbacks)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New Focus view collapses tool calls/results/thinking into one expandable row per turn (toggle via Settings, Command Palette, or `Ctrl+Option+F`/`Ctrl+Alt+F`); persists across sessions and applies to all open sessions immediately. New `focusView` setting, requires v2.1.221+. [[lines 80-291](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/vs-code.md?plain=1#L80-L291)] [[Source](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Section heading/anchor updated to drop the "or ultraplan" reference, reflecting the Ultraplan removal. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/claude-code/web-quickstart.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/web-quickstart#”could-not-create-a-cloud-environment”-or-“no-cloud-environment-available”-when-using-cloud)]

-----

## API changes

### Changed documents

#### [api/admin/analytics](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics)]

* `AnalyticsUser` gains a `type` field (always `"user"`) alongside `id`/`email_address`. [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics.md?plain=1#L147)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics)]
* `AnalyticsUserActor` fields `deleted`, `email`, `name`, `type`, `user_id` are now documented as required (previously all optional). [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics)]

#### [api/admin/analytics/artifacts/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/artifacts/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/artifacts/list)]

* `filter[]` now documents its supported dimensions explicitly: `artifact_type`, `is_shared`, `rbac_group_id`, `user_id`, with value formats for each. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/artifacts/list.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/artifacts/list)]
* `group_by[]` is now typed as an enum of `"rbac_group_id"` / `"user_id"` instead of a free-form string array. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/artifacts/list.md?plain=1#L90)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/artifacts/list)]

#### [api/admin/analytics/chat_projects](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/chat_projects.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects)]

* `created_by` (`AnalyticsUser`) gains a `type` field, always `"user"`. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/chat_projects.md?plain=1#L59)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects)]

#### [api/admin/analytics/chat_projects/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/chat_projects/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)]

* `filter[]` now documents supported dimensions: `project_id`, `rbac_group_id`, `user_id`, with value formats. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/chat_projects/list.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)]
* `created_by.type` field added. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/chat_projects/list.md?plain=1#L121)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/chat_projects/list)]

#### [api/admin/analytics/connectors/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/connectors/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)]

* `filter[]` now documents supported dimensions: `connector_name`, `product`, `rbac_group_id`, `user_id`, with value formats and normalization notes. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/connectors/list.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/connectors/list)]

#### [api/admin/analytics/cost](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]

* New `slack_channel_id` field added to cost result rows and per-user `UserCost` rows, populated when grouping by Slack channel. [[lines 91-93](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost.md?plain=1#L91-L93)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]
* `AnalyticsUserActor` fields now required rather than optional. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost.md?plain=1#L149)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost)]

#### [api/admin/analytics/cost/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]

* `group_by[]` gains a new `"slack_channel_id"` dimension. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]
* New `slack_channel_ids` filter parameter to scope cost data to specific Slack channels. [[lines 116-118](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list.md?plain=1#L116-L118)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]
* Result rows gain a `slack_channel_id` field. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list.md?plain=1#L210)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list)]

#### [api/admin/analytics/cost/list_by_user](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)]

* Same Slack-channel additions: `group_by[]` value `"slack_channel_id"`, a `slack_channel_ids` filter, and a `slack_channel_id` result field. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/cost/list_by_user.md?plain=1#L83)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/cost/list_by_user)]

#### [api/admin/analytics/plugins/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/plugins/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/plugins/list)]

* `filter[]` now documents supported dimensions: `plugin_name`, `product` (`claude_code`/`cowork` only), `rbac_group_id`, `user_id`. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/plugins/list.md?plain=1#L39)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/plugins/list)]

#### [api/admin/analytics/retrieve_summaries](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/retrieve_summaries.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries)]

* New capability: the summaries series can now be scoped to a single RBAC group via `filter[]=rbac_group_id:<id>`. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/retrieve_summaries.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/retrieve_summaries)]

#### [api/admin/analytics/skills/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/skills/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills/list)]

* `filter[]` now documents supported dimensions: `product`, `rbac_group_id`, `share_status`, `skill_name`, `user_id`. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/skills/list.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/skills/list)]

#### [api/admin/analytics/usage](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage)]

* New `slack_channel_id` field added to usage result rows and per-user data. [[lines 95-97](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage.md?plain=1#L95-L97)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage)]

#### [api/admin/analytics/usage/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)]

* `group_by[]` gains `"slack_channel_id"`; new `slack_channel_ids` filter; result rows gain a `slack_channel_id` field. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage/list.md?plain=1#L74)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list)]

#### [api/admin/analytics/usage/list_by_user](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage/list_by_user.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)]

* Same Slack-channel additions as usage/list: `group_by[]` value, `slack_channel_ids` filter, result field. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/usage/list_by_user.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/usage/list_by_user)]

#### [api/admin/analytics/users](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/users.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users)]

* `user` (`AnalyticsUser`) gains a `type` field. [[line 457](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/users.md?plain=1#L457)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users)]

#### [api/admin/analytics/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/users/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users/list)]

* `filter[]` now documents supported dimensions: `project_id`, `rbac_group_id`, `user_id`, including that `project_id` scopes to chat activity in a project and can't combine with `group_by[]`. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/users/list.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users/list)]
* `user.type` field added. [[line 511](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/analytics/users/list.md?plain=1#L511)] [[Source](https://platform.claude.com/docs/en/api/admin/analytics/users/list)]

#### [api/admin/cost_report](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/cost_report.md) [[Source](https://platform.claude.com/docs/en/api/admin/cost_report)]

* `inference_geo` is now a typed enum (`"global"` / `"not_available"` / `"us"`) instead of a freeform string. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/cost_report.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/api/admin/cost_report)]

#### [api/admin/cost_report/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/cost_report/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]

* Same `inference_geo` enum change. [[line 120](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/cost_report/retrieve.md?plain=1#L120)] [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]
* `next_page` cursor format changed from an RFC 3339 timestamp string to an opaque `page_...` token. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/cost_report/retrieve.md?plain=1#L219)] [[Source](https://platform.claude.com/docs/en/api/admin/cost_report/retrieve)]

#### [api/admin/rate_limits](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/rate_limits.md) [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits)]

* Rate-limit entries gain a new `id` field: a stable identifier for the rate-limit group. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/rate_limits.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits)]

#### [api/admin/rate_limits/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/rate_limits/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits/list)]

* Same `id` field addition. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/rate_limits/list.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/api/admin/rate_limits/list)]

#### [api/admin/usage_report](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report)]

* Response actor schemas renamed from `ClaudeCodeUserActor`/`ClaudeCodeAPIActor` to generic `UserActor`/`APIActor`. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report.md?plain=1#L39)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report)]
* `date` field changed from `YYYY-MM-DD` format to an RFC 3339 timestamp at midnight UTC. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report.md?plain=1#L103)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report)]
* `inference_geo` now a typed enum. [[line 252](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report.md?plain=1#L252)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report)]

#### [api/admin/usage_report/retrieve_claude_code](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_claude_code.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]

* Same actor renames (`UserActor`/`APIActor`). [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_claude_code.md?plain=1#L50)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]
* `date` field format changed to an RFC 3339 timestamp. [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_claude_code.md?plain=1#L114)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_claude_code)]

#### [api/admin/usage_report/retrieve_messages](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_messages.md) [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

* `inference_geo` now a typed enum (`"global"`/`"not_available"`/`"us"`). [[line 228](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L228)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]
* `next_page` cursor format changed from timestamp string to opaque `page_...` token. [[line 347](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/usage_report/retrieve_messages.md?plain=1#L347)] [[Source](https://platform.claude.com/docs/en/api/admin/usage_report/retrieve_messages)]

#### [api/admin/workspaces/create](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/create.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

* `allowed_inference_geos`, `default_inference_geo`, and `workspace_geo` are now typed enums (`"global"`/`"us"`, or `"us"` only for `workspace_geo`) instead of freeform strings. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/create.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/create)]

#### [api/admin/workspaces/rate_limits](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/rate_limits.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits)]

* Workspace rate-limit entries gain two new fields: `rate_limit_id` (the id of the org-level rate-limit group being overridden) and `workspace_id`. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/rate_limits.md?plain=1#L67)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits)]

#### [api/admin/workspaces/rate_limits/list](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/rate_limits/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list)]

* Same new fields `rate_limit_id` and `workspace_id`. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/rate_limits/list.md?plain=1#L99)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/rate_limits/list)]

#### [api/admin/workspaces/update](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

* Same enum typing change for `allowed_inference_geos`/`default_inference_geo`. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/api/admin/workspaces/update.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/api/admin/workspaces/update)]

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Compaction is no longer beta: the requirement to include beta header `compact-2026-01-12` was removed, along with the old beta-only supported-models list.
* New "Compatibility" table documents supported models (Fable 5, Mythos 5/Preview, Opus 4.6-5, Sonnet 4.6/5) and supported platforms, now including Claude API, Claude Platform on AWS, Amazon Bedrock, Google Cloud, and Microsoft Foundry (each marked Beta). [[lines 589-594](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/build-with-claude/compaction.md?plain=1#L589-L594)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* New guidance: use your SDK's message-accumulation helper (e.g., `stream.get_final_message()` in Python, `stream.finalMessage()` in TypeScript) to reassemble complete thinking blocks with signatures after streaming, instead of concatenating deltas manually. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/build-with-claude/thinking.md?plain=1#L225)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]
* Clarified Ruby SDK behavior: plain hashes use `display:`, while only the typed `ThinkingConfigAdaptive` class requires the trailing-underscore `display_` param name (previously stated flatly that `display_:` was needed). [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/build-with-claude/thinking.md?plain=1#L171)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

#### [cli-sdks-libraries/libraries/apple-foundation-models](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/cli-sdks-libraries/libraries/apple-foundation-models.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)]

* Clarified billing requirement: using Claude via Apple Foundation Models requires the organization to have an available credit balance or active billing method. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/939646871028932d679c68f5596106622c897ea7/docs-md/api/cli-sdks-libraries/libraries/apple-foundation-models.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)]
