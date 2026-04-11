# [Claude docs changes for April 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c234619cb5d44cd43413f36803bbd5ca1a0f234f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c234619cb5d44cd43413f36803bbd5ca1a0f234f)]

## Executive Summary
- New documentation for Claude in Amazon Bedrock (research preview): a new Messages API endpoint at `/anthropic/v1/messages` runs on AWS-managed infrastructure with zero operator access, currently available in `us-east-1`
- Claude Code 2.1.101 now trusts the OS CA certificate store by default, eliminating extra configuration for enterprise TLS-inspection proxies (CrowdStrike, Zscaler, etc.)
- `/loop` command significantly expanded: self-paced interval mode where Claude chooses the delay, a built-in autonomous maintenance prompt, and `loop.md` customization for project-specific defaults
- Security fix in 2.1.101: command injection vulnerability in the POSIX `which` fallback used by LSP binary detection
- Structured outputs extended to Ruby and PHP SDKs; TypeScript gains `jsonSchemaOutputFormat()` alongside `zodOutputFormat()`

## New Claude Code versions

### [2.1.101](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/versions/2.1.101.md)

#### New features

* Added `/team-onboarding` command to generate a teammate ramp-up guide from your local Claude Code usage
* Added OS CA certificate store trust by default, so enterprise TLS proxies work without extra setup; set `CLAUDE_CODE_CERT_STORE=bundled` to use only the bundled Mozilla CA set
* `/ultraplan` and other remote-session features now auto-create a default cloud environment instead of requiring web setup first

#### Existing feature improvements

* Improved brief mode to retry once when Claude responds with plain text instead of a structured message
* Improved rate-limit retry messages to show which limit was hit and when it resets instead of an opaque seconds countdown
* Improved `claude -p --resume <name>` to accept session titles set via `/rename` or `--name`
* Improved settings resilience: an unrecognized hook event name in `settings.json` no longer causes the entire file to be ignored
* Improved plugin hooks from plugins force-enabled by managed settings to run when `allowManagedHooksOnly` is set
* Improved beta tracing to honor `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_TOOL_DETAILS`, and `OTEL_LOG_TOOL_CONTENT`; sensitive span attributes are no longer emitted unless opted in
* Improved SDK `query()` to clean up subprocess and temp files when consumers `break` from `for await` or use `await using`

#### Major bug fixes

* Fixed a command injection vulnerability in the POSIX `which` fallback used by LSP binary detection
* Fixed a memory leak where long sessions retained dozens of historical copies of the message list in the virtual scroller
* Fixed `--resume`/`--continue` losing conversation context on large sessions when the loader anchored on a dead-end branch instead of the live conversation
* Fixed a hardcoded 5-minute request timeout that aborted slow backends (local LLMs, extended thinking, slow gateways) regardless of `API_TIMEOUT_MS`
* Fixed `permissions.deny` rules not overriding a PreToolUse hook's `permissionDecision: "ask"` — previously the hook could downgrade a deny into a prompt
* Fixed Bedrock SigV4 authentication failing with 403 when `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, or `ANTHROPIC_CUSTOM_HEADERS` set an Authorization header
* Fixed subagents not inheriting MCP tools from dynamically-injected servers
* Fixed sub-agents running in isolated worktrees being denied Read/Edit access to files inside their own worktree
* Fixed Grep tool ENOENT when the embedded ripgrep binary path becomes stale (VS Code extension auto-update, macOS App Translocation); now falls back to system `rg` and self-heals mid-session
* Fixed custom keybindings (`~/.claude/keybindings.json`) not loading on Bedrock, Vertex, and other third-party providers

-----

## Claude Code changes

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` now also applies to the Bedrock Mantle endpoint, not just standard Bedrock. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/amazon-bedrock.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]
* Added `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` to the Mantle-specific environment variables table. [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/amazon-bedrock.md?plain=1#L333)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#mantle-environment-variables)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/loop` updated: both the interval and the prompt are now optional. Omitting the interval lets Claude self-pace between iterations; omitting the prompt runs the built-in maintenance check or `.claude/loop.md` if present. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/commands.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Computer use](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/computer-use.md) [[Source](https://code.claude.com/docs/en/computer-use)]

* New section "Screenshots are downscaled automatically": Claude Code downscales every screenshot before sending it to the model, so Retina and high-DPI displays do not need resolution changes. For example, a 16-inch MacBook Pro at native Retina resolution captures at 3456×2234 and downscales to roughly 1372×887. [[line 99](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/computer-use.md?plain=1#L99)] [[Source](https://code.claude.com/docs/en/computer-use#apps-are-hidden-while-claude-works)]

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Updated cost benchmarks based on enterprise deployment data: average is now ~$13/developer/active day and $150–250/developer/month (previously $6/day and $100–200/month). 90th-percentile cap updated to $30/active day. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/costs.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/costs)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION` description updated to mention it also applies to Bedrock Mantle. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/env-vars.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` description updated to include PowerShell commands (not just Bash). [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/env-vars.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_CODE_CERT_STORE` variable added: comma-separated list of CA certificate sources (`bundled`, `system`). Default is `bundled,system`. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/env-vars.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added a full JSON example showing how to correctly merge multiple hook event types (e.g., `PostToolUse` and `Notification`) into the same `hooks` object, clarifying the correct nesting structure. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/hooks-guide.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/hooks-guide#set-up-your-first-hook)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified that `allowManagedHooksOnly` exempts hooks from plugins that are force-enabled via `enabledPlugins` in managed settings, allowing organizations to distribute vetted hooks through a marketplace while blocking everything else. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/hooks.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP scope hierarchy and precedence now documented as an explicit ordered list: Local (1) > Project (2) > User (3) > Plugin-provided servers (4) > claude.ai connectors (5). Also clarified that plugins and connectors deduplicate by endpoint/URL, not by name. [[line 1163](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/mcp.md?plain=1#L1163)] [[Source](https://code.claude.com/docs/en/mcp#user-scope)]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* PowerShell subprocesses now also inherit the `TRACEPARENT` environment variable for distributed tracing (previously only Bash subprocesses were mentioned). [[line 107](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/monitoring-usage.md?plain=1#L107)] [[Source](https://code.claude.com/docs/en/monitoring-usage#traces-beta)]

#### [Network configuration](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* New "CA certificate store" section: documents that Claude Code now trusts both the bundled Mozilla CA set and the OS certificate store by default, making enterprise TLS-inspection proxies work out of the box. Covers the `CLAUDE_CODE_CERT_STORE` env var (`bundled`, `system`, or both), notes that system CA integration requires the native binary (not the Node.js runtime), and shows how to restrict to one source. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/network-config.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/network-config#ca-certificate-store)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that the `:*` suffix in Bash permission rules (e.g., `Bash(ls:*)`) is not deprecated — it is an equivalent way to write a trailing wildcard, behaving identically to `Bash(ls *)`. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/permissions.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/permissions#wildcard-patterns)]
* Updated `allowManagedHooksOnly` description to clarify that hooks from plugins force-enabled in managed settings `enabledPlugins` are exempt from the block. [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/permissions.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [Run prompts on a schedule](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Major `/loop` documentation overhaul. Added a summary table of all three invocation modes: interval+prompt (fixed schedule), prompt-only (Claude self-paces), and bare `/loop` (built-in maintenance prompt). [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/scheduled-tasks.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#run-a-prompt-repeatedly-with-/loop)]
* New section "Let Claude choose the interval": when the interval is omitted, Claude dynamically picks a delay (1 min–1 hour) based on observed activity. May use the Monitor tool to stream events instead of polling. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/scheduled-tasks.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval)]
* New section "Run the built-in maintenance prompt": bare `/loop` runs an autonomous maintenance loop — continues unfinished work, tends to the PR (review comments, CI failures, conflicts), and runs cleanup passes when nothing else is pending. Irreversible actions only proceed if authorized in the transcript. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/scheduled-tasks.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt)]
* New section "Customize the default prompt with loop.md": `.claude/loop.md` (project-level) or `~/.claude/loop.md` (user-level) replaces the built-in maintenance prompt. Edits take effect on the next iteration; content over 25,000 bytes is truncated. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/scheduled-tasks.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#customize-the-default-prompt-with-loop-md)]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Removed "(public beta)" from the title and beta-related language throughout the page; server-managed settings are now generally available. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/server-managed-settings.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/server-managed-settings)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `allowManagedHooksOnly` description and behavior documentation to clarify that hooks from plugins force-enabled in `enabledPlugins` are loaded; trust is granted by full `plugin@marketplace` ID. [[lines 143, 398](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/settings.md?plain=1#L143)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added clarification that a subagent starts in the main conversation's current working directory; `cd` commands inside a subagent do not persist between Bash/PowerShell calls and do not affect the main conversation's working directory. Use `isolation: worktree` to give the subagent an isolated copy. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/sub-agents.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Expanded Bash tool working directory behavior: `cd` in the main session carries over to later Bash commands as long as it stays within the project directory or an added directory; moving outside causes a reset with a `Shell cwd was reset to <dir>` message appended. `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` disables carry-over entirely. Subagent sessions never carry over working directory changes. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/tools-reference.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/tools-reference#bash-tool-behavior)]
* Added note that the same main-session working-directory reset behavior and `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` apply to PowerShell commands as well. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/tools-reference.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/tools-reference#shell-selection-in-settings-hooks-and-skills)]

#### [Troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Added `CRYPT_E_NO_REVOCATION_CHECK (0x80092012)` as an additional Windows TLS error code that indicates the certificate revocation lookup is blocked by a corporate firewall, alongside the existing `CRYPT_E_REVOCATION_OFFLINE` entry. [[line 294](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/claude-code/troubleshooting.md?plain=1#L294)] [[Source](https://code.claude.com/docs/en/troubleshooting#tls-or-ssl-connection-errors)]

-----

## API changes

### New Documents

#### [Claude in Amazon Bedrock (research preview)](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/claude-in-amazon-bedrock-research-preview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock-research-preview)]

New guide for the Claude in Amazon Bedrock research preview — a new Messages API endpoint at `/anthropic/v1/messages` running on AWS-managed infrastructure with zero operator access. Covers three authentication methods (Bedrock service role, IAM assumed roles, bearer tokens), SDK installation, supported models (Claude Mythos Preview and Claude Haiku 4.5 with `anthropic.` prefix), feature availability (extended thinking, prompt caching, tool use, citations, structured outputs supported; Anthropic-defined tools, Managed Agents, and Batches API not supported), quotas (2M input TPM default, up to 4M without additional approval), data retention, CloudWatch/CloudTrail observability, and support contacts. Currently available in `us-east-1` by invitation only.

### Changed documents

#### [Claude on Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Intro updated to clarify this page covers the current Bedrock integration (`InvokeModel`/`Converse` APIs), and now links to the new research preview page for the Messages API endpoint. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md?plain=1#L3)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

#### [Code execution tool](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Replaced prose model compatibility description with a detailed table listing every supported model and which tool versions (`code_execution_20250825`, `code_execution_20260120`) each one supports. Clarifies that `code_execution_20260120` (REPL persistence + programmatic tool calling) is limited to Opus 4.5+/Sonnet 4.5+ and newer. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Programmatic tool calling](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Replaced the generic compatibility reference with an explicit table of the four models that support `code_execution_20260120`: Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5, and Claude Sonnet 4.5. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Clarified that only the Python SDK's `client.messages.parse()` accepts `output_format` as a convenience parameter; other SDKs require `output_config` directly. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L113)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* TypeScript now supports `jsonSchemaOutputFormat()` in addition to `zodOutputFormat()` for typed JSON Schema literals. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L119)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* PHP SDK now supports structured outputs via classes implementing `StructuredOutputModel` with `outputConfig: ['format' => MyClass::class]`. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L121)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Added a complete CLI example for structured outputs using a YAML heredoc body and `--transform` with GJSON. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L196)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Automatic schema transformation (removing unsupported constraints, updating descriptions) now documented for Ruby and PHP SDKs in addition to Python and TypeScript. [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/c234619cb5d44cd43413f36803bbd5ca1a0f234f/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L224)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
