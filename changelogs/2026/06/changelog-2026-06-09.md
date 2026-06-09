# [Claude docs changes for June 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/28085629a2ddd16c085e18a2dae4ef8f08f2e34f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/28085629a2ddd16c085e18a2dae4ef8f08f2e34f)]

## Executive Summary
- Claude Code 2.1.169 adds `--safe-mode` flag to disable all customizations for troubleshooting, and a `/cd` command to change working directory without breaking prompt cache
- New `disableBundledSkills` setting lets organizations hide bundled skills and built-in slash commands from the model
- Fixed enterprise managed MCP policies not being enforced on reconnect and during first session after install, plus slow cold starts for orgs without remote settings
- API docs clarified that Skills work with all code execution tool versions (`code_execution_20260120` and later), not just the original `code_execution_20250825`
- Advisor tool documentation now notes it accepts generic tool properties: `cache_control`, `allowed_callers`, `defer_loading`, and `strict`

## New Claude Code versions

### [2.1.169](https://github.com/gpambrozio/ClaudeDocs/blob/28085629a2ddd16c085e18a2dae4ef8f08f2e34f/versions/2.1.169.md)

#### New features

* Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE` env var) to start Claude Code with all customizations disabled (CLAUDE.md, plugins, skills, hooks, MCP servers) for troubleshooting
* Added `/cd` command to move a session to a new working directory without breaking the prompt cache mid-session
* Added `disableBundledSkills` setting and `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` env var to hide bundled skills, workflows, and built-in slash commands from the model

#### Existing feature improvements

* `/workflows` now opens immediately even while a turn is in progress
* Improved `TaskCreate` reliability: malformed inputs are repaired automatically and validation errors for unloaded tools include the schema
* Reduced CPU usage while responses stream and during spinner animations
* Restored a default 5-minute idle timeout on Vertex/Foundry so a stalled stream aborts instead of hanging indefinitely; set `API_FORCE_IDLE_TIMEOUT=0` to opt out
* Remote-managed settings with an invalid entry now apply their remaining valid policies and surface the validation error instead of silently dropping the whole payload
* Background sessions now preserve `--ide`, `--chrome`, `--bare`, `--remote-control`, and other flags across retire→wake
* The "CLAUDE.md is too long" warning threshold now scales with the model's context window
* Improved error message shown when an organization has disabled API key authentication

#### Major bug fixes

* Fixed enterprise managed MCP policies (`allowedMcpServers`/`deniedMcpServers`) not being enforced on reconnect, IDE-typed configs, `--mcp-config` servers during first session after install, or before remote settings loaded; also fixed slow cold starts for orgs without remote settings
* Fixed a ~30-50ms UI stall at the start of each turn for macOS users logged in with claude.ai credentials
* Fixed `claude -p` being slow or appearing to hang on Windows while waiting for slash-command/skill scan (regression in 2.1.161)
* Fixed `claude agents --json` omitting blocked and just-dispatched background sessions; added `--all` to include completed sessions, plus new `id` and `state` fields
* Fixed background agents ignoring project-level settings `env` values (e.g. `ANTHROPIC_MODEL`) when dispatched onto a pre-warmed worker
* Fixed stale permission and dialog prompts reappearing every time you reattached to a remote session whose worker had died while waiting on them
* Fixed footer hints (e.g. "esc to interrupt") not showing for users with a custom statusline
* Fixed Remote Control getting stuck on "reconnecting" after resuming a session when an OAuth token refresh happened simultaneously
* Fixed Git Credential Manager's "Connect to GitHub" popup appearing on Windows at startup when background git commands ran without cached credentials
* Fixed untrusted project settings being able to set OTEL client-certificate paths without trust confirmation

-----

## Claude Code changes

No significant changes.

-----

## API changes

### Changed documents

#### [agent-skills/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/28085629a2ddd16c085e18a2dae4ef8f08f2e34f/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Clarified that Skills work with all code execution tool versions: the quickstart examples use `code_execution_20250825`, but Skills also work with newer revisions (`code_execution_20260120` and later) — any version satisfies the Skills requirement as long as its tool `type` and beta header are kept consistent. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/28085629a2ddd16c085e18a2dae4ef8f08f2e34f/docs-md/api/agents-and-tools/agent-skills/quickstart.md?plain=1#L79)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

#### [tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/28085629a2ddd16c085e18a2dae4ef8f08f2e34f/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Added documentation noting that the advisor tool accepts the generic tool properties available on any tool definition: `cache_control`, `allowed_callers`, `defer_loading`, and `strict`, with a reference to the Tool reference for their semantics. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/28085629a2ddd16c085e18a2dae4ef8f08f2e34f/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L101)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
