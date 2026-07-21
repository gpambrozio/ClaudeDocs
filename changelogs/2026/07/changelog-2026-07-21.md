# [Claude docs changes for July 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24)]

## Executive Summary
- Major model launch documented: **Claude Fable 5**, **Claude Mythos 5** (limited availability via Project Glasswing), **Claude Opus 4.8**, and **Claude Sonnet 5** — all with 1M-token context, adaptive thinking on by default, and new migration/pricing guidance.
- Brand-new **"CLI, SDKs & Libraries"** documentation section: the official `ant` CLI, SDK references for Python, TypeScript, C#, Go, Java, PHP, and Ruby, plus new Apple Foundation Models and OpenAI SDK compatibility integrations.
- New comprehensive `claude_api_primer.md` quickstart guide and a full AWS IAM actions reference for Claude Platform on AWS.
- Claude Code **2.1.216** fixes a quadratic slowdown in long sessions, several worktree/git safety issues, and adds a `sandbox.filesystem.disabled` setting alongside various UX improvements (`/fork`, `/context`, `/rewind`).
- Rate limits and pricing tiers overhauled — numbered tiers (1-4, Enterprise) renamed to Start/Build/Scale/Custom with substantially higher throughput, while Priority Tier is closed to new purchases.

## New Claude Code versions

### [2.1.216](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/versions/2.1.216.md)

#### New features

* Added `sandbox.filesystem.disabled` setting to skip filesystem isolation while keeping network egress control

#### Existing feature improvements

* Improved the `/fork` confirmation to one line with the new session's name, `claude attach` id, and a note when the copy shares your checkout
* Improved the `/ultrareview` diff-too-large error to show configured limits, measured diff size, and largest contributing files
* `/context` now shows an explicit warning when the conversation exceeds the context window, and a failed `/compact` displays as an error
* `/rewind` no longer restores or deletes files through symlinks or hard links at tracked paths and reports how many paths it skipped
* Background sessions: `/mcp` and `/install-github-app` now park a "needs input" request in the agent view when no client is attached

#### Major bug fixes

* Fixed a slowdown in long sessions where message normalization cost grew quadratically with the number of turns, causing multi-second stalls and slow resumes
* Fixed auto mode denying commands with "HTTP 401" classifier errors after the OAuth token expired or rotated mid-session
* Fixed Claude Code on the web re-asking the same question and dropping your answer after the session sat idle for a few minutes
* Fixed resumed background agent sessions reverting to the default agent: the agent's prompt and tool restrictions are now restored
* Fixed worktree-isolated subagents redirecting git into the shared checkout via `git -C`, `--git-dir`, or `GIT_DIR`/`GIT_WORK_TREE`
* Fixed worktree sessions landing in another project's leftover worktree when the working directory did not match the selected project
* Fixed `claude daemon stop --any` potentially terminating an unrelated process via a stale legacy daemon lockfile
* Fixed MCP re-authenticate revoking working credentials before the new sign-in succeeds
* Fixed cloud sessions dropping the in-flight message when the session's container restarts mid-turn — the interrupted turn now re-runs on resume instead of leaving the session unresponsive

-----

## Claude Code changes

### Changed documents

#### [agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* `"auto"` permission mode description updated: now says the model classifier approves or denies "permission prompts" (rather than "each tool call"), clarifying that auto mode gates prompts, not every tool call. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)]

#### [custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* New guidance on running the weather tool example end-to-end (`python weather.py` / `npx tsx weather.ts`). [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#call-a-custom-tool)]
* Documents that tool search is now on by default for SDK MCP tools (deferred loading), and adds the `alwaysLoad: true` option (via `extras` in `tool()` or `createSdkMcpServer()`) to keep a tool's full schema always in the initial prompt. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#add-more-tools)]
* Notes example output may now include a `ToolSearch` call since tool search is on by default. [[line 759](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L759)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#example-unit-converter)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Setup instructions expanded: adds `npm init -y`, `npm pkg set type=module`, and `npm install --save-dev tsx` for the TypeScript quickstart, with guidance on CommonJS projects using `.mts` files. [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/overview.md?plain=1#L55)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#get-started)]
* Behavior change: both the TypeScript and Python SDKs now bundle a native Claude Code binary (previously only TypeScript did). [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/overview.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#get-started)]
* New run instructions for the quickstart example (`npx tsx agent.ts`, `uv run agent.py`, `python3 agent.py`). [[lines 153-160](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/overview.md?plain=1#L153-L160)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#get-started)]
* Playwright MCP example now explicitly sets `allowed_tools=["mcp__playwright__*"]` / `allowedTools: ["mcp__playwright__*"]` rather than relying on implicit access. [[line 368](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/overview.md?plain=1#L368)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview#capabilities)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* `auto` permission mode description updated: model classifier approves or denies "permission prompts" rather than "each tool call". [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L105)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#available-modes)]

#### [python](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Agent tool input: `run_in_background` clarified to be background-by-default; new `team_name` field (deprecated, ignored); `mode` field is now deprecated/ignored since subagents inherit the parent session's permission mode. [[lines 2381-2384](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2381-L2384)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agent)]
* New `modelsUsed` field on Agent tool `completed` and `async_launched` results, listing models used in order with consecutive repeats collapsed (requires v2.1.212+); `resolvedModel` semantics clarified for both variants. [[lines 2404-2405](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2404-L2405)] [[lines 2445-2446](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2445-L2446)] [[line 2467](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2467)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agent)]
* `AskUserQuestion`: options gain a new `preview` field; input schema gains `annotations` (per-question preview/notes) and `metadata` (analytics); output schema gains `response` (freeform reply), `annotations`, and `afkTimeoutMs` (set when the dialog auto-resolved due to inactivity). [[line 2485](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2485)] [[lines 2495-2499](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2495-L2499)] [[lines 2517-2521](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/python.md?plain=1#L2517-L2521)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#askuserquestion)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Behavior change: both TypeScript and Python SDKs now bundle a native Claude Code binary (previously TypeScript only). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#setup)]
* `auto` mode description updated: classifier approves/denies "permission prompts" rather than "each tool call". [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L333)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#key-concepts)]

#### [typescript](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `tool()` extras: `searchHint` (capability phrase shown in the deferred-tool list for tool search) and `alwaysLoad` (keeps a tool's schema always in the initial prompt). [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L111)] [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#tool)]
* `createSdkMcpServer()` gains new `instructions` option (server instructions surfaced to the model) and `alwaysLoad` option (disables deferral for every tool on the server). [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L160)] [[lines 172-174](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L172-L174)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#createsdkmcpserver)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* "Needs input" state now also covers an MCP authentication or settings request held by a session with no terminal attached. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-view.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/agent-view#read-session-state)]
* Behavior change: `/install-github-app` and the `/mcp` settings list now work normally while attached to a background session; when nobody is attached, the session surfaces under "Needs input" instead of being refused outright. [[lines 159-160](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/agent-view.md?plain=1#L159-L160)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* New login path documented: gateway sign-in for organizations routing through a cloud gateway, selected via `forceLoginMethod: "gateway"`; it doesn't authenticate against an Anthropic organization so `forceLoginOrgUUID` doesn't apply to it. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/authentication.md?plain=1#L123)] [[line 127](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/authentication.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Behavior change: orphaned plugin versions are now deleted after 14 days (was 7 days). [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/claude-directory.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/claude-directory#what’s-not-shown)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--disallowedTools`: a rule naming `EndConversation` can no longer remove it while any other tool remains. [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/cli-reference.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--tools`: a list that omits `EndConversation` no longer removes it; `""` removes it only when no MCP tools remain. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/cli-reference.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` variable: caps content-bearing OpenTelemetry attribute length (default 61440 / 60 KB); requires v2.1.214+. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/env-vars.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_PID` variable: Claude Code sets this in subprocesses it spawns; used on Linux to refuse a `pkill` pattern matching itself; requires v2.1.214+. [[line 327](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/env-vars.md?plain=1#L327)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT` variable (and LOGRECORD/SPAN variants): standard OTel SDK attribute length limit, combined with `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` to determine the effective cap. [[line 377](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/env-vars.md?plain=1#L377)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `OTEL_LOG_RAW_API_BODIES`: inline body truncation now uses the configurable content limit instead of a fixed 60 KB. [[line 379](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/env-vars.md?plain=1#L379)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error section: "Failed to update spend limit or auto-reload" — covers rejected `/usage-credits` spend-limit/auto-reload changes (v2.1.216). [[line 346](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L346)] [[Source](https://code.claude.com/docs/en/errors#failed-to-update-spend-limit-or-auto-reload)]
* New error section: "Socket is closed" — a Windows-behind-corporate-proxy dropped-tunnel failure is now automatically retried (fixed in v2.1.214, previously fatal). [[line 647](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L647)] [[Source](https://code.claude.com/docs/en/errors#socket-is-closed)]
* New error section: "Context exceeds the token limit" — explains the new `/context` warning shown when usage exceeds the context/compaction window, naming `/compact`/`/clear` as remedies (v2.1.216). [[line 748](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L748)] [[Source](https://code.claude.com/docs/en/errors#context-exceeds-the-token-limit)]
* New error section: "Settings file exceeds the 2MiB limit" — `--settings` now rejects files over 2MiB or non-regular files, fixing unbounded memory growth (v2.1.214). [[line 1082](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1082)] [[Source](https://code.claude.com/docs/en/errors#settings-file-exceeds-the-2mib-limit)]
* New error section: "Workspace not trusted when starting Remote Control" — `claude remote-control`/`claude rc` now exits with a clear message when the workspace isn't trusted (v2.1.214+). [[line 1095](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1095)] [[Source](https://code.claude.com/docs/en/errors#workspace-not-trusted-when-starting-remote-control)]
* New error section: "Diff is too large for ultrareview" — `/code-review ultra` and `claude ultrareview` now refuse oversized diffs/PRs up front, reporting file/line limits and largest contributing files (v2.1.216). [[line 1143](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1143)] [[Source](https://code.claude.com/docs/en/errors#diff-is-too-large-for-ultrareview)]
* New error section: "Failed to resume the conversation" — `claude --resume` picker now shows a clear failure message and exits instead of hanging (v2.1.216). [[line 1157](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1157)] [[Source](https://code.claude.com/docs/en/errors#failed-to-resume-the-conversation)]
* New error section: "pkill pattern matches the Claude Code process" — on Linux, Claude Code now tests `pkill` patterns via `pgrep` first and refuses ones matching its own PID (v2.1.214). [[line 1264](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1264)] [[Source](https://code.claude.com/docs/en/errors#pkill-pattern-matches-the-claude-code-process)]
* New error section: "Session agent no longer available" — resuming a session whose custom `--agent` no longer exists now warns and falls back to default tools/system prompt (v2.1.216). [[line 1312](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1312)] [[Source](https://code.claude.com/docs/en/errors#session-agent-no-longer-available)]
* New "Rewind warnings" section — `/rewind` now skips (rather than overwrites) symlinks/hard-links/non-regular files and reports a partial-restore warning (v2.1.216). [[line 1364](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L1364)] [[Source](https://code.claude.com/docs/en/errors#restored-the-code-but-skipped-files)]
* Additional fixes: auto-mode classifier now auto-refreshes an expired/rotated OAuth token and retries once [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L208)]; the "waiting for API response" stall banner now waits 90s (not 20s) during advisor calls [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L111)]; PDF error messages and size limits updated (100 pages, 20MB) [[line 840](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/errors.md?plain=1#L840)]. [[Source](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New guidance: in screen reader mode, Claude Code always uses the classic renderer except in attached background sessions; `/tui fullscreen` in other screen-reader sessions now prints an explanation instead of switching. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/fullscreen.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* `WorktreeCreate`/`WorktreeRemove` now also fire for background sessions (creation and deletion). [[lines 441-442](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks-guide.md?plain=1#L441-L442)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]
* `SessionStart` matcher/source gains new `fork` value (in addition to `startup`, `resume`, `clear`, `compact`). [[line 600](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks-guide.md?plain=1#L600)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PreToolUse`/`PostToolUse` now explicitly skip for `EndConversation` tool calls. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* New `fork` value for `SessionStart` matcher/`source`, covering `--fork-session`, `/fork`, and `/branch`. [[line 198](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* New guidance on `if` condition directory-pattern matching: a single-segment pattern like `Edit(src/**)` now matches only the top-level `src` directory (was any-depth before v2.1.214); use `Edit(**/src/**)` for any-depth matching. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]
* Behavior change: a hook exiting 2 with JSON that fails output-schema validation now still blocks, instead of silently proceeding (fixed v2.1.214). [[line 602](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L602)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-output)]
* `PostToolUse` Agent tool_response gains new `modelsUsed` field (v2.1.212+) and clarifies `resolvedModel`/backgrounding-transition semantics. [[lines 1373-1374](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L1373-L1374)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-input)]
* `WorktreeCreate` now also fires for background sessions, with path-safety hardening — absolute paths containing `.`/`..` segments or passing through a symlink under the repo root are now refused (new in v2.1.216, closes a symlink-escape risk). [[line 2320](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L2320)] [[lines 2366-2367](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L2366-L2367)] [[Source](https://code.claude.com/docs/en/hooks#worktreecreate)]
* `WorktreeRemove` now also fires when deleting a background session's worktree, with the same symlink-safety verification (v2.1.216). [[line 2375](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/hooks.md?plain=1#L2375)] [[Source](https://code.claude.com/docs/en/hooks#worktreeremove)]

#### [large-codebases](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/large-codebases.md) [[Source](https://code.claude.com/docs/en/large-codebases)]

* Added guidance to run `/context` and check the **Memory files** list to confirm which CLAUDE.md files loaded. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/large-codebases.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/large-codebases#layer-claude-md-files-by-directory)]
* New note: JSON examples show one setting at a time, so add the `worktree` key alongside existing keys rather than replacing the settings file. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/large-codebases.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/large-codebases#check-out-only-the-directories-you-need)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added guidance to confirm CLAUDE.md loaded via `/context` and the **Memory files** list. [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/memory.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/memory#set-up-a-project-claude-md)]
* `/init` behavior changed: now reads Cursor rules and Copilot rules by default; reading `AGENTS.md`, Devin/Windsurf/Cline rules now requires `CLAUDE_CODE_NEW_INIT=1`. [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/memory.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/memory#agents-md)]
* Auto memory toggle now explicitly saves `autoMemoryEnabled` to user settings by default; set it per-project to disable for a single project. [[line 300](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/memory.md?plain=1#L300)] [[Source](https://code.claude.com/docs/en/memory#auto-memory)]
* `/memory` now lists CLAUDE.md entries for files that don't exist yet, and selecting one creates it. [[line 354](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/memory.md?plain=1#L354)] [[Source](https://code.claude.com/docs/en/memory#view-and-edit-with-/memory)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New resource attribute value: `service.name` is now `claude-code-desktop` for sessions started from the Code tab in Claude Desktop (vs `claude-code` for terminal sessions). [[lines 1101-1109](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/monitoring-usage.md?plain=1#L1101-L1109)] [[Source](https://code.claude.com/docs/en/monitoring-usage#service-information)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* New required hosts added to the allowlist: `claude.com` (sign-in redirect, doc lookups), `http-intake.logs.us5.datadoghq.com` and `browser-intake-us5-datadoghq.com` (telemetry/error reports), `formulae.brew.sh` (Homebrew update checks), and `code.claude.com` (doc lookups). [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/network-config.md?plain=1#L119)] [[lines 127-130](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/network-config.md?plain=1#L127-L130)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]
* New env var `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` disables both Datadog telemetry hosts at once. [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/network-config.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New carve-out: deny/ask rules apply in every mode including `bypassPermissions`, but can't block `EndConversation` while any other tool remains. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permission-modes.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Bare-name and glob-pattern deny/ask rules now documented to be unable to remove `EndConversation` while any other tool remains. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permissions.md?plain=1#L30)] [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permissions.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/permissions#manage-permissions)]
* "Wrappers" section expanded: now also strips shell builtins `command` and `builtin`, and zsh's `noglob`; does NOT strip `command -v` or zsh's `nocorrect`. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permissions.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/permissions#process-wrappers)]
* New behavior: Claude Code strips a leading assignment of known-safe env vars before matching Bash allow rules (e.g. `NODE_ENV=test npm test` matches `Bash(npm test *)`). [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/permissions.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/permissions#process-wrappers)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `WorktreeCreate`/`WorktreeRemove` hook events now also fire for background sessions. [[lines 118-119](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/plugins-reference.md?plain=1#L118-L119)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]
* Plugin version retention/cleanup grace period doubled from 7 to 14 days. [[lines 637-693](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/plugins-reference.md?plain=1#L637)] [[Source](https://code.claude.com/docs/en/plugins-reference#environment-variables)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New caveat: the startup trust dialog never saves trust for your home directory, so Remote Control must be started from a project directory. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/remote-control.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/remote-control#requirements)]
* Reminder-notification behavior changed: reminders can now appear in any connected session, not only ones where you manually turned on Remote Control. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/remote-control.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/remote-control#session-url-reminders)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Behavior change (v2.1.214): when a routine trigger fires, the session now receives the saved prompt as its assigned task and acts on it directly, rather than as an untrusted notification it could refuse. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/routines.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Permission-rules description updated with the `EndConversation` exception. [[line 265](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/sandboxing.md?plain=1#L265)] [[Source](https://code.claude.com/docs/en/sandboxing#permission-rules)]

#### [security-guidance](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/security-guidance.md) [[Source](https://code.claude.com/docs/en/security-guidance)]

* Python requirement lowered to 3.7+ generally, but agentic commit review and model-backed reviews on third-party providers now require Python 3.10+; the plugin now prefers versioned interpreters `python3.13`-`python3.10`. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/security-guidance.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/security-guidance#prerequisites)]
* Fallback behavior clarified: first-party auth falls back to single-shot review on SDK/Python issues, while third-party providers instead skip model-backed review entirely. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/security-guidance.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/security-guidance#prerequisites)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `deny` setting documentation now notes it can't remove `EndConversation` while any other tool remains. [[line 349](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/settings.md?plain=1#L349)] [[Source](https://code.claude.com/docs/en/settings#permission-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New documented pattern: using `${CLAUDE_SKILL_DIR}` identically in both the skill body and an `allowed-tools` Bash rule lets a bundled script run without a permission prompt. Requires Claude Code v2.1.129+. [[lines 259-273](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/skills.md?plain=1#L259-L273)] [[Source](https://code.claude.com/docs/en/skills#available-string-substitutions)]
* `disallowed-tools` frontmatter field documented to be unable to remove `EndConversation` while any other tool remains. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/skills.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New trigger: the status line script now also runs once when a session starts (including on resume), fixing a prior double-run flicker on resume (v2.1.216). [[lines 127-135](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/statusline.md?plain=1#L127-L135)] [[Source](https://code.claude.com/docs/en/statusline#how-status-lines-work)]
* New `effort` field added to `subagentStatusLine` per-task data, reporting the subagent's configured reasoning effort; requires v2.1.214+. [[line 1025](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/statusline.md?plain=1#L1025)] [[Source](https://code.claude.com/docs/en/statusline#subagent-status-lines)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `EndConversation` added to the list of tools unavailable to subagents (it can only end the main conversation). [[line 275](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/sub-agents.md?plain=1#L275)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* New note: in screen reader mode, fullscreen rendering doesn't apply — Claude Code always renders as plain scrolling text except in attached background sessions. [[line 256](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/terminal-config.md?plain=1#L256)] [[Source](https://code.claude.com/docs/en/terminal-config#switch-to-fullscreen-rendering)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New tool added to the reference table: `EndConversation` — ends the session in rare cases of sustained abusive input or on explicit user request to demonstrate it; requires v2.1.213+. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/tools-reference.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/tools-reference)]
* New "EndConversation tool behavior" section: it never prompts and can't be blocked by deny/ask rules while any other tool remains, subagents never get it, and it requires v2.1.213+, a recent-enough model, and an interactive terminal session (not `-p`, Agent SDK, VS Code, GitHub Actions, or Claude Code on the web; not available on Bedrock/Vertex/Microsoft Foundry/cloud gateway sign-ins). [[lines 146-169](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/tools-reference.md?plain=1#L146-L169)] [[Source](https://code.claude.com/docs/en/tools-reference#endconversation-tool-behavior)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* New troubleshooting entry: `claude update`/`claude doctor` hang when a directory (rather than a file) exists at one of the scanned shell-config paths. Fixed in v2.1.214+. [[lines 523-525](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/troubleshoot-install.md?plain=1#L523-L525)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#claude-update-or-claude-doctor-hangs)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* New behavior: when the branch shares no merge base with the base branch, `/code-review ultra` (and `claude ultrareview`) now offers a whole-repository review fallback instead of refusing to run. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/ultrareview.md?plain=1#L23)] [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/claude-code/ultrareview.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-from-the-cli)]

-----

## API changes

### New Documents

#### [introducing-claude-fable-5-and-claude-mythos-5](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)]

This page announces Claude Fable 5 (`claude-fable-5`) and Claude Mythos 5 (`claude-mythos-5`, limited release via Project Glasswing), both sharing a 1M-token context window, 128k max output, and pricing of $10/MTok input and $50/MTok output. The key differentiator is that Fable 5 includes safety classifiers that can decline requests (returning `stop_reason: "refusal"`), while Mythos 5 does not; the doc details refusal handling, server-side/client-side/manual fallback options, and billing rules. Both models launch June 9, 2026, carry 30-day data retention as Covered Models, always run adaptive thinking, and support features like effort, task budgets, memory tool, code execution, and compaction.

#### [model-ids-and-versions](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/model-ids-and-versions.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)]

This page documents Claude's model ID and versioning scheme, explaining that starting with the Claude 4.6 generation, IDs use a dateless format (e.g. `claude-sonnet-5`, `claude-opus-4-8`) representing a permanently pinned snapshot rather than an evergreen alias, unlike pre-4.6 dated IDs which have separate rolling aliases. It clarifies platform-specific formatting differences across the Claude API, Amazon Bedrock, and Google Cloud, and notes that surrounding serving infrastructure can still change and cause minor behavioral drift even though weights are fixed per ID.

#### [whats-new-claude-4-8](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/whats-new-claude-4-8.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8)]

This page covers Claude Opus 4.8, a successor to Opus 4.7 with the same 1M-token context and adaptive thinking support. New at launch: mid-conversation system messages (no beta header needed), publicly documented `stop_details` refusal categories, an effort default of `high` across all surfaces, a research-preview "fast mode," and a lower prompt-cache minimum of 1,024 tokens.

#### [whats-new-sonnet-5](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/whats-new-sonnet-5.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5)]

This page introduces Claude Sonnet 5 as a drop-in upgrade for Sonnet 4.6, with adaptive thinking now on by default, manual extended thinking removed, and sampling parameters no longer accepted. It highlights a new tokenizer producing roughly 30% more tokens for the same text, notes Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards, and states pricing is unchanged at $3/$15 per MTok with an introductory rate of $2/$10 through August 31, 2026.

#### [classification](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/classification.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/classification)]

This new guide explains when to use Claude instead of traditional ML for classification tasks, surveys common classification use cases by industry, and walks through implementation steps: choosing a model, building a starter prompt, developing test cases, and running evaluations against metrics like accuracy, F1 score, consistency, and bias/fairness.

#### [claude-platform-on-aws-iam-actions](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/claude-platform-on-aws-iam-actions.md) [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions)]

This reference exhaustively catalogs the 65 IAM actions in the `aws-external-anthropic` namespace that gate access to Claude Platform on AWS, organized by resource area, and includes a full route-to-action mapping table with CloudTrail classification. It documents the five AWS-managed policies and provides worked example policies for scenarios like single-workspace inference, per-customer isolation, and ZDR feature lockdown, calling out several IAM gotchas that could silently over-permission a workspace.

#### [prompting-claude-fable-5](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-fable-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)]

This new guide covers prompting and scaffolding patterns specific to Claude Fable 5 and Claude Mythos 5, framed around long-horizon autonomy: effort-level selection, grounding progress claims during long runs, explicit action boundaries, parallel subagent delegation, and building a persistent memory system. It introduces a "send-to-user" client-side tool pattern for long asynchronous runs and warns that echoing reasoning as response text can trigger the new `reasoning_extraction` refusal category.

#### [prompting-claude-opus-4-8](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)]

This new model-specific guide details how to tune prompts for Claude Opus 4.8, covering response verbosity, effort/thinking-depth settings (recommending `xhigh` for coding/agentic work), tool-use triggering, subagent spawning control, and default design/frontend aesthetics. It gives detailed treatment of code-review harnesses and computer-use resolution tradeoffs.

#### [prompting-claude-sonnet-5](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)]

This new guide covers Sonnet-5-specific prompting patterns, most notably that adaptive thinking is on by default and manual extended thinking is removed entirely (400 error), as are sampling parameters. It recommends "propose options before building" prompts as a replacement technique and gives a cross-model effort mapping for migration.

#### [claude_api_primer](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/claude_api_primer.md) [[Source](https://platform.claude.com/docs/en/claude_api_primer)]

This primer is a condensed, example-driven introduction to the core mechanics of the Claude Messages API, covering model IDs, request/response patterns, multi-turn conversations, response prefilling, vision inputs, extended/adaptive thinking, tool definitions and use, and streaming via server-sent events. It's structured as a fast-reference guide with runnable code snippets rather than exhaustive prose, serving as a quick-start cheat sheet for wiring up a working integration.

#### [cli/authentication](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/cli/authentication.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication)]

Details every credential option for the new `ant` CLI: interactive OAuth login (including headless flow and workspace binding), requesting elevated `org:admin` scope, using the `ANTHROPIC_API_KEY` environment variable, checking the active credential via `ant auth status`, and managing multiple workspace-bound profiles.

#### [cli/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/cli/quickstart.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart)]

Introduces the `ant` CLI as a terminal client for the Claude API, contrasting it with `curl` by highlighting typed flags/YAML input, `@path` file inlining, `--transform` response filtering, and automatic pagination. Walks through installation, authentication, sending a first request, and installing shell completions.

#### [cli/scripting](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/cli/scripting.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)]

Covers task-oriented automation workflows built on the `ant` CLI, centered on version-controlling API resources (agent, environment, session YAML definitions) and keeping them synced via `beta:agents`/`beta:environments`/`beta:sessions` commands, plus shell scripting patterns for chaining CLI output into follow-up commands.

#### [cli/using](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/cli/using.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using)]

Explains the `ant` CLI's cross-endpoint input/output mechanics: the `resource action` command structure, global flags, output formats and the interactive explorer TUI, reshaping responses with GJSON `--transform` expressions, and the three ways to pass request bodies.

#### [libraries/apple-foundation-models](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/libraries/apple-foundation-models.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models)]

Documents Claude for Foundation Models, a beta Swift package that conforms Claude to Apple's Foundation Models `LanguageModel` protocol, covering installation, model/effort selection, authentication, streaming, structured output via `@Generable`, tool use, image input, and error handling, plus a list of Messages API features not exposed through this integration.

#### [libraries/openai-sdk](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/libraries/openai-sdk.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk)]

Describes the OpenAI SDK compatibility layer that lets developers call Claude using an official OpenAI SDK by changing only the base URL, API key, and model name, positioned as a testing/comparison tool. Details key behavioral differences and exhaustive tables of request/response field and header support status.

#### [middleware](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/middleware.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/middleware)]

Documents the middleware/interceptor hook available across the Anthropic client SDKs for running code before a request is sent and after a response is received, covering registration, chaining/ordering rules, interaction with a custom HTTP client, and the built-in refusal-fallback middleware.

#### [cli-sdks-libraries/overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

The landing page for the new "CLI, SDKs, and libraries" section, introducing the `ant` CLI, client SDKs (Python, TypeScript, C#, Go, Java, PHP, Ruby), and framework-specific libraries (Apple Foundation Models, OpenAI SDK compatibility), and distinguishing them from higher-level agent runtimes like Claude Code and Claude Managed Agents.

#### [sdks/csharp](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/csharp.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/csharp)]

The official Anthropic C# SDK (`Anthropic` NuGet package, beta), replacing the earlier community tryAGI SDK. Covers client construction, async streaming, typed exceptions, retries/timeouts, pagination, and an `IChatClient` integration for Microsoft.Extensions.AI including MCP tool interop, plus platform-specific packages for Bedrock, Google Cloud, Foundry, and Claude Platform on AWS.

#### [sdks/go](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/go.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go)]

The Anthropic Go SDK (`github.com/anthropics/anthropic-sdk-go`), detailing `omitzero`-based request field semantics, union types, error handling via `*anthropic.Error`, retries/timeouts, pagination, and platform integrations for Vertex AI, Amazon Bedrock (including a new `NewMantleClient`), and Claude Platform on AWS.

#### [sdks/java](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/java.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java)]

The Anthropic Java SDK reference, using a builder pattern with both synchronous and `CompletableFuture`-based async clients on OkHttp. Documents streaming helpers, tool use with automatic JSON schema derivation via Jackson, batches, file uploads, a typed exception hierarchy, retries, pagination, and platform integrations.

#### [sdks/php](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/php.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php)]

Documents the official Anthropic PHP library (beta), installed via Composer alongside a PSR-18 HTTP client. Covers named-parameter usage, SSE-based streaming, typed exception handling, automatic retries, auto-paginating iterators, and platform integration clients for Bedrock, Vertex, AWS, and Microsoft Foundry.

#### [sdks/python](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/python.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python)]

The Anthropic Python SDK reference, covering both the synchronous `Anthropic` client and `AsyncAnthropic`, streaming via `client.messages.stream()`, tool use with `@beta_tool`/`tool_runner`, message batches, structured error handling, retries, auto-pagination, and a Pydantic-based type system.

#### [sdks/ruby](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby)]

The Anthropic Ruby gem, providing typed access via `net/http` with connection pooling and Yard/RBS/RBI type definitions for Sorbet. Covers SSE-based streaming, structured tool-calling with an automatic tool-execution loop via `beta.messages.tool_runner`, typed errors, retries, pagination, and platform integrations.

#### [sdks/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/cli-sdks-libraries/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript)]

Covers the `@anthropic-ai/sdk` npm package, supporting Node 20+, Deno, Bun, Cloudflare Workers, and Vercel Edge. Details SSE streaming, Zod/JSON-Schema tool definitions run through `beta.messages.toolRunner()`, MCP helpers for bridging MCP servers into the Claude API, message batches, typed errors, retries/timeouts, and pagination.

### Changed documents

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/glossary.md) [[Source](https://platform.claude.com/docs/en/about-claude/glossary)]

* No significant changes.

#### [model-deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* New announcement that Claude Mythos Preview will be retired July 21, 2026, with migration guidance to Claude Mythos 5. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/model-deprecations.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]
* Model status table updated for the new lineup: `claude-fable-5` and `claude-opus-4-8` added as Active; `claude-opus-4-1-20250805` moved to Deprecated (retiring August 5, 2026); `claude-opus-4-20250514` and `claude-sonnet-4-20250514` moved to Retired; `claude-sonnet-5` added as Active. [[lines 75-89](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/model-deprecations.md?plain=1#L75-L89)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]
* New "API parameter deprecations" section: `temperature`, `top_p`, `top_k` are deprecated on Claude Opus 4.7+ (including Opus 4.8 and Sonnet 5) and now return a 400 error when set to a non-default value. [[lines 209-217](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/model-deprecations.md?plain=1#L209-L217)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [choosing-a-model](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/choosing-a-model.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

* Fast mode now supported on both Claude Opus 4.8 and Opus 4.7 (previously only Opus 4.6); fast mode on Opus 4.7 is now deprecated, removal July 24, 2026. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]
* New "Effort" criterion added to key selection factors, recommending tuning effort over switching models, with `xhigh` best for coding/agentic use on Opus 4.8/4.7. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]
* New introduction of Claude Fable 5 and Claude Mythos 5: 1M-token context by default, up to 128k output tokens, always-on adaptive thinking, priced at $10/$50 per MTok. [[lines 61-63](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L61-L63)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]
* Model selection matrix updated: Opus 4.7/Sonnet 4.6 rows replaced with Claude Opus 4.8 and Claude Sonnet 5. [[lines 69-70](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L69-L70)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

#### [migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* New "Claude API skill" automated migration workflow via `/claude-api migrate`, detecting Bedrock/Claude Platform on AWS/Google Cloud/Microsoft Foundry clients. [[lines 13-21](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md?plain=1#L13-L21)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* New "Migrating to Claude Mythos 5" section: always-on adaptive thinking, prefill returns 400, requires 30-day data retention, plus a sub-guide for migrating from Claude Mythos Preview. [[lines 23-99](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md?plain=1#L23-L99)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* New "Migrating to Claude Fable 5" section (from Claude Opus 4.8): pricing change, 30-day retention requirement, adaptive thinking always on (behavior change), new safety classifiers with `stop_reason: "refusal"`, opt-in beta `fallbacks` parameter, and a lower prompt-caching minimum. [[lines 101-203](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md?plain=1#L101-L203)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* New "Migrating to Claude Opus 4.8" section: effort now defaults to `high` across all surfaces, sampling/prefill parameters return 400, mid-conversation system messages now accepted, refusal `stop_details` now publicly documented. [[lines 191-421](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md?plain=1#L191-L421)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* New "Migrating to Claude Sonnet 5" section: introductory pricing $2/$10 per MTok through August 31, 2026; breaking changes for manual extended thinking and sampling parameters (400 errors); new tokenizer producing ~30% more tokens; adaptive thinking on by default; new cybersecurity safety classifiers; Priority Tier not available. [[lines 596-741](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/migration-guide.md?plain=1#L596-L741)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Default recommendation changed to Claude Opus 4.8 for complex agentic coding/enterprise work, pointing to Claude Fable 5 for the highest-capability workloads. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* New "Claude Fable 5 and Claude Mythos 5" section: Fable 5 is generally available starting June 9, 2026; Mythos 5 is limited-availability via Project Glasswing. [[lines 15-19](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/overview.md?plain=1#L15-L19)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Latest models comparison table replaced: now shows Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, and Claude Haiku 4.5, with updated pricing and extended thinking now "No" for all top-tier models (replaced by adaptive thinking). [[lines 23-45](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/overview.md?plain=1#L23-L45)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* New note: the `effort` parameter defaults to `high` on Opus 4.8 (all surfaces) and Sonnet 5 (Claude API and Claude Code). [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/models/overview.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [pricing](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added new model pricing rows for Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Sonnet 5 (introductory $2/$10 through August 31, 2026, then $3/$15). [[lines 17-26](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/pricing.md?plain=1#L17-L26)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* New "Claude Platform on AWS pricing" and "Claude in Microsoft Foundry pricing" sections: billed via Claude Consumption Units (CCUs) at $0.01/CCU through AWS/Azure Marketplace. [[lines 74-126](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/pricing.md?plain=1#L74-L126)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Fast mode pricing restructured into a per-model table; fast mode for Opus 4.7 is now deprecated (removal July 24, 2026), Opus 4.6 fast mode already discontinued. [[lines 163-170](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/pricing.md?plain=1#L163-L170)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Rate-limit tier names changed from numbered tiers (Tier 1-4, Enterprise) to named tiers (Start, Build, Scale). [[lines 460-462](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/pricing.md?plain=1#L460-L462)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [content-moderation](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/content-moderation.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

* Cost estimate example updated to reference Claude Opus 4.8 (was 4.7), with rescaled cost figures. [[lines 92-106](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/content-moderation.md?plain=1#L92-L106)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

#### [customer-support-chat](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/customer-support-chat.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

* Added a new "Prerequisites" section specifying required Claude API key, Python 3.9+, and package installation. [[lines 7-18](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/customer-support-chat.md?plain=1#L7-L18)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]
* Recommended model updated from Claude Opus 4.7 to Claude Opus 4.8. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/customer-support-chat.md?plain=1#L141)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

#### [legal-summarization](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/legal-summarization.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]

* Recommended/example model updated from Claude Opus 4.7 to Claude Opus 4.8 throughout. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/legal-summarization.md?plain=1#L157)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]
* Fixed a stray closing parenthesis bug in the meta-summarization prompt f-string. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/legal-summarization.md?plain=1#L270)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/overview)]

* No significant changes.

#### [ticket-routing](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/ticket-routing.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing)]

* Added a new "Prerequisites" section requiring a Claude API key, familiarity with an existing ticketing system, and a sample set of historical tickets. [[lines 7-11](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/about-claude/use-case-guides/ticket-routing.md?plain=1#L7-L11)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing)]

#### [claude-api-skill](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

* Language coverage expanded: the skill now covers 8 languages (Python, TypeScript, C#, Go, Java, PHP, Ruby, cURL) for both the Messages API and Managed Agents. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]
* New "Refusal fallback configuration" migration capability: adds `stop_reason: "refusal"` handling and sets up a fallback retry path when the target model is Claude Fable 5. [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L137)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

#### [admin](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin.md) [[Source](https://platform.claude.com/docs/en/api/admin)]

* No significant changes.

#### [admin/api_keys](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys)]

* New callout clarifies that end users should view/create their own API keys in Console Settings → API keys, distinguishing this Admin API page from personal key management. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys)]

#### [admin/api_keys/list](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/list.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

* Same new callout added directing users to Settings → API keys for personal key management vs. this Admin API listing endpoint. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/list.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/list)]

#### [admin/api_keys/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

* Page renamed to "Retrieve API Key (Admin API)" with an expanded description clarifying this requires an Admin API key and never returns the key's secret value. [[lines 11-15](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/retrieve.md?plain=1#L11-L15)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/retrieve)]

#### [admin/api_keys/update](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/update.md) [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

* Same new callout added pointing users to Settings → API keys for personal key management vs. this Admin API update endpoint. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/admin/api_keys/update.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/admin/api_keys/update)]

#### [beta-headers](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/beta-headers.md) [[Source](https://platform.claude.com/docs/en/api/beta-headers)]

* New endpoint-specific beta headers documented: `mcp-tunnels-2026-06-22` for `/v1/tunnels` and `agent-memory-2026-07-22` for `/v1/memory_stores`. [[lines 75-77](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/beta-headers.md?plain=1#L75-L77)] [[Source](https://platform.claude.com/docs/en/api/beta-headers)]
* New guidance: on memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`, and sending both returns a 400 error. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/beta-headers.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/api/beta-headers)]

#### [claude-code/routines-fire](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/claude-code/routines-fire.md) [[Source](https://platform.claude.com/docs/en/api/claude-code/routines-fire)]

* `500 api_error` guidance expanded to recommend retrying with exponential backoff and contacting support with the request ID. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/claude-code/routines-fire.md?plain=1#L150)] [[Source](https://platform.claude.com/docs/en/api/claude-code/routines-fire)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* New `409 conflict_error` HTTP error code documented for resource-state conflicts. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/api/errors)]
* New documented behavior: official SDKs automatically retry transient failures with exponential backoff twice by default, honoring `retry-after`. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/api/errors)]
* New "SDK error types" section documenting typed exception classes per language. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md?plain=1#L67)] [[Source](https://platform.claude.com/docs/en/api/errors)]
* New "Thinking blocks cannot be modified" validation-error section explaining the 400 error returned when thinking blocks are edited before resubmission. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md?plain=1#L157)] [[Source](https://platform.claude.com/docs/en/api/errors)]
* New "Outbound web identity federation disabled (Claude Platform on AWS)" section. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/errors.md?plain=1#L169)] [[Source](https://platform.claude.com/docs/en/api/errors)]

#### [ip-addresses](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/ip-addresses.md) [[Source](https://platform.claude.com/docs/en/api/ip-addresses)]

* New guidance for Claude Platform on AWS: the inbound endpoint resolves to AWS IP ranges, while outbound tool calls still originate from Anthropic's listed ranges. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/ip-addresses.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/ip-addresses)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/overview.md) [[Source](https://platform.claude.com/docs/en/api/overview)]

* New authentication method: `Authorization: Bearer <token>` via short-lived tokens through Workload Identity Federation. [[lines 18-50](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/overview.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/api/overview)]
* API keys now have configurable expiration, set at creation time. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/overview.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/api/overview)]
* Entirely new "Pagination" section documenting the `page`/`next_page`/`prev_page` cursor scheme and the alternate `after_id`/`before_id` scheme. [[lines 132-146](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/overview.md?plain=1#L132-L146)] [[Source](https://platform.claude.com/docs/en/api/overview)]
* Rate limit increases now self-service via a "Request rate limit increase" button, replacing the prior "contact sales" flow. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/overview.md?plain=1#L162)] [[Source](https://platform.claude.com/docs/en/api/overview)]

#### [rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Usage tiers renamed/restructured from Tier 1-4 to Start/Build/Scale/Custom with a simplified monthly spend cap table. [[lines 36-42](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/rate-limits.md?plain=1#L36-L42)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]
* Messages API rate limits increased substantially across the board (RPM from 50 to 1,000; ITPM/OTPM raised 10-65x depending on model); new rows for Claude Fable 5 and Claude Sonnet 5. [[lines 145-154](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/rate-limits.md?plain=1#L145-L154)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]
* New "Requesting higher limits" section: self-service button replaces the old Contact Sales flow. [[lines 211-221](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/rate-limits.md?plain=1#L211-L221)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [service-tiers](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/service-tiers.md) [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

* Priority Tier capacity commitments are no longer available for new purchase; only existing commitments continue through their contract end date. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/service-tiers.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/service-tiers)]
* Priority Tier supported-models list updated: now includes Claude Fable 5 and Claude Opus 4.8, but excludes Claude Sonnet 5 and Claude Mythos 5. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/service-tiers.md?plain=1#L131)] [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

#### [supported-regions](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/supported-regions.md) [[Source](https://platform.claude.com/docs/en/api/supported-regions)]

* No significant changes.

#### [versioning](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/api/versioning.md) [[Source](https://platform.claude.com/docs/en/api/versioning)]

* No significant changes.

#### [adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* No significant changes.

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Removed mention of "spend alerts" as a billing feature. [[line 547](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L547)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

#### [extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* No significant changes.

#### [files](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* No significant changes.

#### [claude-prompting-best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

* Page restructured into three parts and rewritten to reference Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Sonnet 5. [[lines 7-10](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L7-L10)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]
* All inline Opus-4.7-specific guidance removed and replaced with short pointer sections linking out to new dedicated per-model prompting guides. [[lines 17-27](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L17-L27)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]
* New guidance that setting `budget_tokens` now returns a 400 error on Claude Opus 4.7+, Claude Fable 5, and Claude Mythos 5. [[line 349](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L349)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

* New pointer to the general prompt-engineering blog post as a resource distinct from Claude-specific techniques. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/overview.md?plain=1#L40)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)]

#### [prompting-tools](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/prompting-tools.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools)]

* Prompt generator Colab notebook link moved to the maintained `anthropic/claude-cookbooks` GitHub repo notebook. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/build-with-claude/prompt-engineering/prompting-tools.md?plain=1#L25)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools)]

#### [cmek](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Dropped the statement that "Multi-region keys and EU key residency are not yet supported." [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/manage-claude/cmek.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [data-residency](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/manage-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/data-residency)]

* No significant changes.

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Workbench legacy console is being sunset (access ends August 17, 2026) and experimental prompt-tools APIs are being retired alongside it. [[lines 13-16](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md?plain=1#L13-L16)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Launched **Claude Sonnet 5**, **Claude Opus 4.8**, **Claude Fable 5**, and **Claude Mythos 5**, each with dated entries detailing context window, tokenizer, thinking, and refusal-handling changes. [[lines 44-98](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md?plain=1#L44-L98)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Rate limits raised across the API; tiers consolidated into Start/Build/Scale. [[lines 57-59](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md?plain=1#L57-L59)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Launched **Claude Platform on AWS** with AWS billing/IAM auth for Messages API, Files API, Batches, Managed Agents, Skills, and code execution. [[lines 156-158](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md?plain=1#L156-L158)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Workload Identity Federation reached general availability for OIDC-based API authentication. [[lines 168-170](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/overview.md?plain=1#L168-L170)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/system-prompts.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts)]

* Added new model sections for Claude Fable 5 (June 9, 2026) and Claude Opus 4.8 (May 28, 2026) system prompt history. [[lines 9-15](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/release-notes/system-prompts.md?plain=1#L9-L15)] [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/resources/overview.md) [[Source](https://platform.claude.com/docs/en/resources/overview)]

* Added system card entries for Claude Sonnet 5, Claude Fable 5/Mythos 5, Claude Opus 4.8, and Claude Mythos Preview, updating the model-cards list to reflect current releases. [[lines 9-105](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/resources/overview.md?plain=1#L9-L105)] [[Source](https://platform.claude.com/docs/en/resources/overview)]

#### [develop-tests](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/develop-tests.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]

* No significant changes.

#### [eval-tool](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/eval-tool.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool)]

* The Console's built-in prompt generator is now stated to be powered by Claude Sonnet 4.5, updated from the previously documented Claude Opus 4.1. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/eval-tool.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/eval-tool)]

#### [increase-consistency](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

* Updated the list of models that don't support response prefilling to add Claude Fable 5, Claude Mythos 5, and Claude Opus 4.8. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md?plain=1#L27)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

#### [mitigate-jailbreaks](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)]

* Page substantially rewritten to distinguish jailbreaks/direct prompt injection from indirect prompt injection. [[lines 9-16](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md?plain=1#L9-L16)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)]
* New "Indirect prompt injection" section adds concrete guardrail techniques: keep untrusted content in `tool_result` blocks, disclose content provenance, JSON-encode untrusted content, apply least-privilege access, and screen tool outputs with a classifier. [[lines 27-52](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md?plain=1#L27-L52)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)]

#### [reduce-hallucinations](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)]

* No significant changes.

#### [reduce-latency](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-latency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)]

* Added a new "Next steps" section linking to Reduce hallucinations and Streaming messages guides. [[lines 88-96](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-latency.md?plain=1#L88-L96)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)]

#### [reduce-prompt-leak](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)]

* Updated the list of models that don't support prefilling to add Claude Fable 5, Claude Mythos 5, and Claude Opus 4.8. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/66d59bbc221d5cfe93765fbb76a82e5ec6aa4c24/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak.md?plain=1#L24)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)]
