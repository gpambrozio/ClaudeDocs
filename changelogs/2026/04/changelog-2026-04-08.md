# [Claude docs changes for April 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7edee33) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7edee33)]

## Executive Summary
- New User Profiles API (beta) allows attributing API requests to specific end-users via `/v1/user_profiles` endpoints
- Claude Mythos Preview (Project Glasswing) announced as an invitation-only research preview model for defensive cybersecurity workflows
- Amazon Bedrock Mantle endpoint support added to Claude Code: native Messages API shape (`CLAUDE_CODE_USE_MANTLE=1`) as an alternative to the legacy Invoke API
- Default effort level changed to "high" for API-key, Team, Enterprise, and third-party provider (Bedrock/Vertex/Foundry) users; Pro/Max subscribers remain at "medium"
- New `stop_details` field added to message responses to provide structured information about refusals (cyber/bio policy categories)

## New Claude Code versions

### [2.1.94](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/versions/2.1.94.md)

#### New features

* Added support for Amazon Bedrock Mantle endpoint via `CLAUDE_CODE_USE_MANTLE=1`
* Added compact `Slacked #channel` header with clickable channel link for Slack MCP send-message tool calls
* Added `keep-coding-instructions` frontmatter field support for plugin output styles
* Added `hookSpecificOutput.sessionTitle` to `UserPromptSubmit` hooks for setting the session title
* Plugin skills declared via `"skills": ["./"]` now use the skill's frontmatter `name` for the invocation name instead of the directory basename

#### Existing feature improvements

* Changed default effort level from medium to high for API-key, Bedrock/Vertex/Foundry, Team, and Enterprise users (control this with `/effort`)
* Improved `--resume` to resume sessions from other worktrees of the same repo directly instead of printing a `cd` command

#### Major bug fixes

* Fixed agents appearing stuck after a 429 rate-limit response with a long Retry-After header
* Fixed Console login on macOS silently failing with "Not logged in" when the login keychain is locked or out of sync
* Fixed plugin skill hooks defined in YAML frontmatter being silently ignored
* Fixed plugin hooks failing with "No such file or directory" when `CLAUDE_PLUGIN_ROOT` was not set
* Fixed scrollback showing the same diff repeated and blank pages in long-running sessions
* Fixed Shift+Space inserting the literal word "space" in search inputs
* Fixed hyperlinks opening two browser tabs inside tmux running in an xterm.js-based terminal (VS Code, Hyper, Tabby)
* Fixed `FORCE_HYPERLINK` environment variable being ignored when set via `settings.json` `env`
* Fixed SDK/print mode not preserving the partial assistant response in conversation history when interrupted mid-stream
* Fixed CJK and multibyte text being corrupted with U+FFFD in stream-json input/output when chunk boundaries split a UTF-8 sequence
* [VSCode] Added a warning banner when `settings.json` files fail to parse

### [2.1.96](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/versions/2.1.96.md)

#### Major bug fixes

* Fixed Bedrock requests failing with `403 "Authorization header is missing"` when using `AWS_BEARER_TOKEN_BEDROCK` or `CLAUDE_CODE_SKIP_BEDROCK_AUTH` (regression in 2.1.94)

-----

## Claude Code changes

### New Documents

#### [Claude in Amazon Bedrock (Mantle)](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

New guide for the Claude in Amazon Bedrock research preview offering, which exposes the native Anthropic Messages API at `/anthropic/v1/messages` (branded "Mantle"), distinct from the legacy Bedrock Invoke API. Covers three authentication paths (Bedrock service role, IAM assumed roles, bearer tokens), SDK installation, supported features, regional availability (us-east-1 only), quotas, data retention policy, and observability via CloudWatch/CloudTrail. Notably, Anthropic-defined tools (Web Search, Files API, Skills, etc.) are not supported on this offering.

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New "Use the Mantle endpoint" section added, documenting how to enable the Mantle endpoint via `CLAUDE_CODE_USE_MANTLE=1`, how to select Mantle-format model IDs (`anthropic.` prefix), how to run Mantle alongside the legacy Invoke API, how to route through an LLM gateway, and specific Mantle environment variables. [[line 244](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/amazon-bedrock.md?plain=1#L244)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#aws-guardrails)]
* New Mantle troubleshooting section added for 403 (access not granted), 400 (wrong model ID format), and missing Mantle status issues. [[line 330](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/amazon-bedrock.md?plain=1#L330)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#region-issues)]

#### [Claude Directory](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* New "Application data" section added documenting everything Claude Code writes to `~/.claude` during sessions. Includes tables for auto-swept files (transcripts, tool results, file snapshots, debug logs, paste/image cache) and persistent files (prompt history, statsig cache, stats-cache, backups). Documents plaintext storage implications and how to reduce credential exposure. Also includes a "Clear local data" guide. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/claude-directory.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/claude-directory#check-what-loaded)]
* Added installed plugins location (`~/.claude/plugins/`) with 7-day orphan cleanup note to the "What's not shown" table.

#### [Code Review](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* New "Rate and reply to findings" section: each review comment now includes 👍/👎 buttons for one-click feedback. Anthropic collects reaction counts to tune the reviewer. Describes how to request a fresh review via `@claude review once`. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/code-review.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/code-review#rate-and-reply-to-findings)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Clarified that when selecting a session from another worktree in the `/resume` picker, Claude Code now resumes it directly without requiring a directory switch. [[line 568](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/common-workflows.md?plain=1#L568)] [[Source](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)]

#### [Data Usage](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Updated local caching description: sessions are stored as plaintext JSONL under `~/.claude/projects/` for 30 days by default, configurable via `cleanupPeriodDays`. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/data-usage.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/data-usage#data-retention)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Three new Mantle-related variables: `ANTHROPIC_BEDROCK_MANTLE_BASE_URL`, `CLAUDE_CODE_SKIP_MANTLE_AUTH`, `CLAUDE_CODE_USE_MANTLE`.
* Added default values for previously undocumented timeouts: `BASH_DEFAULT_TIMEOUT_MS` (2 min), `BASH_MAX_TIMEOUT_MS` (10 min), `MCP_TIMEOUT` (30s), `MCP_TOOL_TIMEOUT` (~28 hours).
* `API_TIMEOUT_MS` now documents its maximum value (2147483647) and warns that exceeding it causes immediate failures.

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Exit code behavior clarified: stdout for most events is now written to the debug log (not verbose mode). Any non-zero exit (other than 2) shows a one-line `<hook name> hook error` notice in the transcript; full stderr goes to the debug log. [[line 473](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md?plain=1#L473)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-output)]
* New clarification: only exit code 2 blocks an action; exit code 1 is non-blocking (exception: `WorktreeCreate` aborts on any non-zero exit). [[line 491](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md?plain=1#L491)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-output)]
* `suppressOutput` JSON field now omits stdout from the debug log (previously suppressed verbose mode output). [[line 556](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md?plain=1#L556)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* New `sessionTitle` field added to `UserPromptSubmit` hook output, allowing hooks to set the session title (same effect as `/rename`). [[line 784](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md?plain=1#L784)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit-decision-control)]
* Debug instructions updated: use `--debug-file <path>` to write to a known location, or `--debug` to find the log at `~/.claude/debug/<session-id>.txt`. [[line 2261](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks.md?plain=1#L2261)] [[Source](https://code.claude.com/docs/en/hooks#windows-powershell-tool)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Updated debug technique: verbose mode (`Ctrl+O`) now shows a one-line summary per hook; full execution details go to the debug log. Instructions updated to use `--debug-file` and `tail -f`. [[line 800](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks-guide.md?plain=1#L800)] [[Source](https://code.claude.com/docs/en/hooks-guide#json-validation-failed)]
* Non-zero exit code description updated to match hooks.md changes. [[line 446](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/hooks-guide.md?plain=1#L446)] [[Source](https://code.claude.com/docs/en/hooks-guide#hook-output)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Ctrl+L` behavior changed from "Redraw the screen" to "Clear prompt input" (clears typed text, keeps conversation history). [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/interactive-mode.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `app:redraw` is now unbound (was Ctrl+L). New `chat:clearInput` action added, bound to Ctrl+L. [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/keybindings.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/keybindings#app-actions)]

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New "Mantle model IDs" section: entries in `availableModels` starting with `anthropic.` are routed to the Mantle endpoint. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/model-config.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/model-config#merge-behavior)]
* Default effort level updated: Pro/Max subscribers default to medium; all others (API key, Team, Enterprise, Bedrock/Vertex/Foundry) now default to high. [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/model-config.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [Output Styles](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Plugins can now ship output styles in an `output-styles/` directory. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/output-styles.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/output-styles#create-a-custom-output-style)]

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* When a skill path points to a directory containing a `SKILL.md` directly (e.g. `"skills": ["./"]`), the frontmatter `name` field now determines the invocation name (stable across install methods). Directory basename is used as fallback. [[line 372](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/plugins-reference.md?plain=1#L372)] [[Source](https://code.claude.com/docs/en/plugins-reference#path-behavior-rules)]
* Plugin cache versioning documented: each installed version is a separate directory; orphaned versions are removed 7 days after a plugin update or uninstall. [[line 464](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/plugins-reference.md?plain=1#L464)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New "Model not found or not accessible" section with troubleshooting steps for when the API rejects a configured model name, including priority order to check and how to clear stale values. [[line 586](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/troubleshooting.md?plain=1#L586)] [[Source](https://code.claude.com/docs/en/troubleshooting#403-forbidden-after-login)]

#### [Ultraplan](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/ultraplan.md) [[Source](https://code.claude.com/docs/en/ultraplan)]

* Added minimum version requirement: v2.1.91 or later.
* Clarified that Ultraplan is not available when using Amazon Bedrock, Google Vertex AI, or Microsoft Foundry (runs on Anthropic's cloud infrastructure). [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/claude-code/ultraplan.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/ultraplan)]

-----

## API changes

### New Documents

#### [Claude in Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

New guide for the "Claude in Amazon Bedrock" research preview (Mantle). This new offering exposes the Anthropic Messages API shape at `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`, using AWS credentials and standard SSE streaming. Distinct from the existing legacy Bedrock integration (Invoke API). Covers three auth methods, SDK support (`anthropic[bedrock]`), supported and unsupported features, regions (us-east-1 only), quotas (2M TPM default), data retention (30 days), observability, and support contacts.

#### [User Profiles](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta/user_profiles.md) [[Source](https://platform.claude.com/docs/en/api/beta/user_profiles)]

New beta API section for User Profiles (`/v1/user_profiles`), requiring the `user-profiles-2026-03-24` beta header. Provides CRUD operations to create, list, retrieve, and update user profiles, plus a Create Enrollment URL endpoint. The `BetaUserProfile` object includes id, created_at, metadata (free-form key-value), trust_grants, type, updated_at, and optional external_id.

### Changed documents

#### [Models Overview](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Added a note about Claude Mythos Preview (Project Glasswing): an invitation-only research preview model for defensive cybersecurity workflows, offered separately with no self-serve sign-up. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/models/overview.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Google Vertex AI now documented as having three endpoint types: global, multi-region, and regional (previously only two were described). [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/models/overview.md?plain=1#L41)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Third-party platform pricing section now separately describes AWS Bedrock (2 endpoint types) and Google Vertex AI (3 endpoint types: global, multi-region, regional). Regional and multi-region endpoints include a 10% premium. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/pricing.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Claude Mythos Preview added to the list of models with the full 1M token context window at standard pricing. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/about-claude/pricing.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [Agent Loop](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/agent-loop.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

* Both Python and TypeScript SDKs now leave `effort` unset by default; the underlying engine resolves a model-dependent default (previously TypeScript defaulted to `"high"`). [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/agent-loop.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]
* `plan` permission mode description updated: read-only tools now run; only tools that make changes are blocked. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/agent-loop.md?plain=1#L148)] [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

#### [Custom Tools](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/custom-tools.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/custom-tools)]

* Error handling behavior corrected: an uncaught exception from a tool handler no longer stops the agent loop — it is wrapped by the MCP server and surfaces to Claude as a tool error result. Using `isError: true` is preferred because it gives control over the error message Claude sees. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/custom-tools.md?plain=1#L224)] [[Source](https://platform.claude.com/docs/en/agent-sdk/custom-tools)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/permissions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

* `plan` mode now documented to allow read-only tools (Read, Grep, Glob, WebFetch) while blocking tools that modify state (file edits, Bash). [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/permissions.md?plain=1#L79)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

#### [Skills (SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/skills.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/skills)]

* `allowedTools` must now be paired with `permissionMode: "dontAsk"` to deny unlisted tools. Without this, unlisted tools fall through to the active permission mode rather than being blocked. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/skills.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/agent-sdk/skills)]

#### [Streaming vs Single Mode](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/streaming-vs-single-mode.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)]

* Hook integration removed from the "not supported" list for single message input mode (hooks now work in single mode). [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agent-sdk/streaming-vs-single-mode.md?plain=1#L114)] [[Source](https://platform.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)]

#### [Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Model compatibility table replaced with a single statement: the tool is available on all supported Claude models using `code_execution_20250825`.
* Added note: for Claude Mythos Preview, code execution is supported on Claude API and Microsoft Foundry only (not Amazon Bedrock or Google Vertex AI). [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* New `output_file_too_large` error type added for bash tool when command output exceeds the maximum size. [[line 350](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L350)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Define Tools](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/define-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

* Claude Mythos Preview does not support forced tool use: requests with `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", ...}` return a 400 error. Only `auto` and `none` are supported. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/define-tools.md?plain=1#L148)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

#### [Tool Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Claude Mythos Preview added to the list of supported models for tool search. [[line 362](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L362)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

#### [Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Claude Mythos Preview added to the dynamic filtering support list (alongside Opus 4.6 and Sonnet 4.6).
* Added platform note: web fetch is supported for Mythos Preview on Claude API and Microsoft Foundry only (not Amazon Bedrock or Google Vertex AI). [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Claude Mythos Preview added to dynamic filtering support (alongside Opus 4.6 and Sonnet 4.6).
* Added platform note: web search for Mythos Preview is available on Claude API, Microsoft Foundry, and Google Vertex AI — not Amazon Bedrock. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

#### [Beta](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Two new beta headers added: `output-300k-2026-03-24` and `user-profiles-2026-03-24`. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* New `BetaRefusalStopDetails` object added to the `BetaMessage` response: a `stop_details` field with `category` ("cyber" or "bio") and `explanation`, providing structured information about refusals. [[line 14688](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta.md?plain=1#L14688)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* New User Profiles section added (CRUD endpoints) with `BetaUserProfile`, `BetaUserProfileEnrollmentURL`, and `BetaUserProfileTrustGrant` models.
* Skill and SkillVersion response model schemas (`SkillCreateResponse`, `SkillListResponse`, `SkillDeleteResponse`, `VersionCreateResponse`, etc.) added to the beta API reference.

#### [Beta Messages Create](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* New `user_profile_id` optional body parameter added: used to attribute a request to a specific user profile when acting on behalf of a party other than your organization. [[line 4518](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta/messages/create.md?plain=1#L4518)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* `stop_details` field added to the `BetaMessage` response with structured refusal information. [[line 5445](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/beta/messages/create.md?plain=1#L5445)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* New HTTP status code documented: `504 timeout_error` — request timed out while processing, with a recommendation to use streaming for long-running requests. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/errors.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/api/errors)]
* Prefill limitation expanded: Claude Mythos Preview added alongside Opus 4.6 as models that return a 400 error when a prefilled last assistant message is included. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/errors.md?plain=1#L110)] [[Source](https://platform.claude.com/docs/en/api/errors)]

#### [Messages](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* New `stop_details` field added to the `Message` object: a `RefusalStopDetails` with `category` ("cyber" or "bio"), `explanation`, and `type: "refusal"`. [[line 5220](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/messages.md?plain=1#L5220)] [[Source](https://platform.claude.com/docs/en/api/messages)]
* `RawMessageDeltaEvent.delta` now includes `stop_details` alongside `stop_reason` and `stop_sequence`. [[line 9447](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/messages.md?plain=1#L9447)] [[Source](https://platform.claude.com/docs/en/api/messages)]

#### [Messages Create](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* `stop_details` field added to the returned `Message` object with structured refusal details (`RefusalStopDetails`). [[line 4384](https://github.com/gpambrozio/ClaudeDocs/blob/7edee33/docs-md/api/api/messages/create.md?plain=1#L4384)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]
